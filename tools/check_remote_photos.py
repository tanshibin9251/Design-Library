"""Verify JPEG source dimensions in memory; never save image files.

Usage: python tools/check_remote_photos.py path/to/images.json
The manifest is read-only. Requests use fm=jpg with no size parameter to avoid
mistaking an upscaled delivery rendition for the original source resolution.
"""
import concurrent.futures
import json
from pathlib import Path
import struct
import sys
import urllib.request
from urllib.parse import urlsplit


def dimensions(url):
    if urlsplit(url).hostname != 'images.unsplash.com':
        raise ValueError('Only the explicitly selected Unsplash image CDN is supported')
    request = urllib.request.Request(url + '?fm=jpg&q=80', headers={'User-Agent': 'DesignLibrary-ImageCheck/1.0'})
    with urllib.request.urlopen(request, timeout=45) as stream:
        if stream.read(2) != b'\xff\xd8':
            raise ValueError('Source is not JPEG')
        scanned = 2
        while scanned < 2_000_000:
            value = stream.read(1)
            scanned += 1
            if not value:
                break
            if value != b'\xff':
                continue
            marker = stream.read(1)
            scanned += 1
            while marker == b'\xff':
                marker = stream.read(1)
                scanned += 1
            if not marker:
                break
            code = marker[0]
            if code in {0x00, 0x01, 0xD8} or 0xD0 <= code <= 0xD7:
                continue
            if code in {0xD9, 0xDA}:
                break
            raw = stream.read(2)
            if len(raw) != 2:
                break
            size = struct.unpack('>H', raw)[0]
            if size < 2:
                break
            payload = stream.read(size - 2)
            scanned += size
            if code in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
                height, width = struct.unpack('>HH', payload[1:5])
                return width, height
    raise ValueError('Could not find JPEG dimensions')


def verify(item):
    width, height = dimensions(item['url'])
    if min(width, height) < 1080 or max(width, height) < 1920:
        raise ValueError(f'{item["id"]}: source {width}x{height} is below the HD requirement')
    return {'id': item['id'], 'width': width, 'height': height}


if __name__ == '__main__':
    manifest = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(verify, manifest['images']))
    print(json.dumps(results, indent=2))
