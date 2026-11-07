"""Integration tests using local temporary Git repositories; no network."""
import contextlib
import io
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import publish_deploy


class PublishTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='dl-publish-test-', ignore_cleanup_errors=True)
        self.base = Path(self.temporary.name)
        self.remote = self.base / 'remote.git'
        self.source = self.base / 'source'
        self.source.mkdir()
        self.run_git('init', '--bare', str(self.remote))
        self.run_git('init', '-b', 'main', str(self.source))
        self.run_git('config', 'user.name', 'Test')
        self.run_git('config', 'user.email', 'test@example.invalid')
        self.run_git('remote', 'add', 'origin', str(self.remote))
        (self.source / 'source-only.txt').write_text('Never deploy source')
        (self.source / '.gitignore').write_text('public_html/\n')
        self.run_git('add', '.')
        self.run_git('commit', '-m', 'Source')
        self.run_git('push', 'origin', 'main')
        self.sha = self.run_git('rev-parse', 'HEAD')
        self.output = self.source / 'public_html'
        self.output.mkdir()
        (self.output / 'index.php').write_text('Website v1')
        (self.output / '.htaccess').write_text('DirectoryIndex index.php')
        self.environment = patch.dict(os.environ, {
            'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main',
            'GITHUB_SHA': self.sha, 'GITHUB_STEP_SUMMARY': ''})
        self.root = patch.object(publish_deploy, 'ROOT', self.source)
        # Output validation has a separate full-build integration check.
        self.check = patch.object(publish_deploy, 'check')
        self.environment.start()
        self.root.start()
        self.check.start()

    def tearDown(self):
        self.environment.stop()
        self.root.stop()
        self.check.stop()
        self.temporary.cleanup()

    def run_git(self, *args, remote=False):
        command = ['git']
        if remote:
            command.extend(['--git-dir', str(self.remote)])
        command.extend(args)
        return subprocess.run(command, cwd=self.source, text=True, check=True,
                              capture_output=True).stdout.strip()

    def publish(self):
        with contextlib.redirect_stdout(io.StringIO()):
            publish_deploy.publish()

    def test_bootstrap_update_and_noop_preserve_main_and_history(self):
        self.publish()
        first = self.run_git('rev-parse', 'deploy', remote=True)
        tree = self.run_git('ls-tree', '--name-only', 'deploy', remote=True)
        self.assertEqual(set(tree.splitlines()), {'.htaccess', 'index.php'})
        self.assertEqual(self.run_git('rev-list', '--count', 'deploy', remote=True), '1')
        self.assertEqual(self.run_git('rev-parse', 'HEAD'), self.sha)
        self.assertEqual(self.run_git('status', '--porcelain'), '')
        self.publish()
        self.assertEqual(self.run_git('rev-parse', 'deploy', remote=True), first)
        (self.output / 'index.php').write_text('Website v2')
        self.publish()
        self.assertEqual(self.run_git('rev-parse', 'deploy^', remote=True), first)
        self.assertEqual(self.run_git('show', 'deploy:index.php', remote=True), 'Website v2')
        self.assertEqual(self.run_git('rev-parse', 'HEAD'), self.sha)

    def test_refuses_other_branches(self):
        with patch.dict(os.environ, {'GITHUB_REF': 'refs/heads/feature'}):
            with self.assertRaises(SystemExit):
                self.publish()

    def test_stale_run_does_not_create_deploy(self):
        (self.source / 'source-only.txt').write_text('New source')
        self.run_git('add', 'source-only.txt')
        self.run_git('commit', '-m', 'New source')
        self.run_git('push', 'origin', 'main')
        self.run_git('checkout', '--detach', self.sha)
        self.publish()
        self.assertEqual(self.run_git('ls-remote', '--heads', 'origin', 'deploy'), '')


if __name__ == '__main__':
    unittest.main()
