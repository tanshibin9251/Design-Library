"""Publish a checked public_html tree without changing the main checkout.

Run by GitHub Actions. An isolated Git index builds the deploy commit; existing
deploy history is preserved and pushes are fast-forward only (never forced).
"""
import os
from pathlib import Path
import subprocess
import tempfile

from check_public_build import check

ROOT = Path(__file__).resolve().parent.parent


def git(*args, env=None, input=None):
    return subprocess.run(['git', *args], cwd=ROOT, env=env, input=input,
                          text=True, check=True, capture_output=True).stdout.strip()


def publish():
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise SystemExit('Publishing is only enabled inside GitHub Actions.')
    if os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise SystemExit('Only the main branch may publish.')
    output = ROOT / 'public_html'
    check(output)
    source = git('rev-parse', 'HEAD')
    if source != os.environ.get('GITHUB_SHA'):
        raise SystemExit('Checkout does not match the triggering source commit.')
    # A queued run must not publish an older main after a newer push.
    main_ref = git('ls-remote', '--heads', 'origin', 'refs/heads/main')
    if not main_ref or main_ref.split()[0] != source:
        print('main has advanced; the newer workflow run will publish instead.')
        return
    remote = git('ls-remote', '--heads', 'origin', 'refs/heads/deploy')
    parent = None
    if remote:
        git('fetch', '--no-tags', 'origin', 'refs/heads/deploy')
        parent = git('rev-parse', 'FETCH_HEAD')
    with tempfile.TemporaryDirectory(prefix='design-library-index-') as temporary:
        env = dict(os.environ)
        env.update(GIT_INDEX_FILE=str(Path(temporary) / 'index'),
                   GIT_AUTHOR_NAME='github-actions[bot]',
                   GIT_AUTHOR_EMAIL='41898282+github-actions[bot]@users.noreply.github.com',
                   GIT_COMMITTER_NAME='github-actions[bot]',
                   GIT_COMMITTER_EMAIL='41898282+github-actions[bot]@users.noreply.github.com')
        git_dir = git('rev-parse', '--absolute-git-dir')
        # --force includes .htaccess and ignores source-branch ignore patterns.
        git('--git-dir', git_dir, '--work-tree', str(output), '-C', str(output),
            'add', '--all', '--force', '--', '.', env=env)
        tree = git('write-tree', env=env)
        if parent and tree == git('rev-parse', f'{parent}^{{tree}}'):
            print('Website is unchanged; deploy branch already matches.')
            return
        args = ['commit-tree', tree]
        if parent:
            args.extend(['-p', parent])
        commit = git(*args, env=env, input=f'Build website from main {source}\n')
    git('push', 'origin', f'{commit}:refs/heads/deploy')
    print(f'Published deploy commit {commit} from main {source}')
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a', encoding='utf-8') as stream:
            stream.write(f'Website published to `deploy`.\n\nSource: `{source}`\n\nDeploy: `{commit}`\n')


if __name__ == '__main__':
    publish()
