"""Read-only checks for the files that will be published to Hostinger."""
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'build'))
import catalog
import dlib
import paths as public_paths


def check(output):
    output = Path(output).resolve()
    if not output.is_dir():
        raise ValueError(f'Missing build directory: {output}')
    allowed = {'index.php', '.htaccess', 'robots.txt', 'assets', 'api',
               'previews', 'includes', 'data'}
    unexpected = {p.name for p in output.iterdir()} - allowed
    if unexpected:
        raise ValueError(f'Unexpected public root files: {sorted(unexpected)}')
    for relative in ('index.php', '.htaccess', 'assets/app.js', 'assets/app.css',
                     'includes/shell.html', 'includes/.htaccess',
                     'data/manifest.json', 'data/.htaccess', 'api/catalog.json'):
        target = output / relative
        if not target.is_file() or target.stat().st_size == 0:
            raise ValueError(f'Missing or empty required file: {relative}')
    if any(p.is_symlink() for p in output.rglob('*')):
        raise ValueError('Symlinks must not be published')
    public = json.loads((output / 'api/catalog.json').read_text(encoding='utf-8'))
    expected = catalog.make_catalog(public=True)
    actual_ids = {item['id'] for item in public['items']}
    if actual_ids != {item['id'] for item in expected['items']}:
        raise ValueError('Public catalog does not match source')
    if any(item.get('local_only') for item in public['items']):
        raise ValueError('A local_only item appears in the public catalog')
    if public['counts'] != expected['counts']:
        raise ValueError('Public catalog counts do not match source')
    for item in public['items']:
        for endpoint, url in item.get('api', {}).items():
            # Imported document templates have only a raw -site.zip export.
            if item.get('format') == 'documents' and endpoint in {
                'site_json', 'html_zip', 'php_zip'
            }:
                continue
            target = (output / url.lstrip('/')).resolve()
            if not target.is_relative_to(output) or not target.is_file():
                raise ValueError(f'Missing public endpoint: {url}')
    for item in catalog.make_catalog()['items']:
        if not item.get('local_only'):
            continue
        if item['id'] in actual_ids:
            raise ValueError(f'Restricted item is public: {item["id"]}')
        # Check both current and legacy paths, including thumbnail copies.
        slug = item['slug']
        for candidate in output.rglob('*'):
            if slug in candidate.parts or candidate.stem in {slug, f't-{slug}', f'e-{slug}'}:
                raise ValueError(f'Restricted output remains: {candidate.relative_to(output)}')
        if item['kind'] == 'asset':
            source = ROOT / item['files']['file']
            if (output / 'api/graphic/assets' / item['category'] / source.name).exists():
                raise ValueError(f'Restricted asset is public: {slug}')
    for template in dlib.template_slugs():
        item = dlib.load_template(template, full=False)
        if item['license'] == 'local_only' or item['format'] != 'documents':
            continue
        relative = public_paths.tpl_rel(template, item['ind'])
        if not (output / f'api/website/templates/{relative}/{template}-site.zip').is_file():
            raise ValueError(f'Missing imported template archive: {template}')
    archives = list(output.rglob('*.zip'))
    for archive in archives:
        with zipfile.ZipFile(archive) as package:
            bad = package.testzip()
            if bad:
                raise ValueError(f'Corrupt archive entry: {archive.name}: {bad}')
            for name in package.namelist():
                entry = Path(name)
                if entry.is_absolute() or '..' in entry.parts:
                    raise ValueError(f'Unsafe archive path: {archive.name}: {name}')
    count = sum(p.is_file() for p in output.rglob('*'))
    print(f'Public build checked: {count} files, {len(archives)} valid ZIPs; no local_only catalog entries')


if __name__ == '__main__':
    check(ROOT / 'public_html')
