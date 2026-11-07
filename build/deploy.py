# -*- coding: utf-8 -*-
"""把 public_html/ 上传到 Hostinger（读取 .vscode/sftp.json 的连接信息；也可以直接把 public_html 里的内容打 zip 在 File Manager 解压）（读取 .vscode/sftp.json 的连接信息）。

用法：  python build/deploy.py          先 build 再全量上传
        python build/deploy.py --changed  只传大小有变的文件（可能漏掉同大小的改动）
不会删除服务器上的其它文件（跟 sftp.json 的 delete:false 一致）。
"""
import ftplib
import io
import json
import re
import sys
from pathlib import Path

import build

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = Path(__file__).parent.parent
CFG = json.loads(re.sub(r"//.*", "", (ROOT / ".vscode/sftp.json").read_text(encoding="utf-8")))
SITE = ROOT / CFG.get("context", "public_html")


def connect():
    try:
        f = ftplib.FTP_TLS()
        f.connect(CFG["host"], CFG["port"], timeout=60)
        f.login(CFG["username"], CFG["password"])
        f.prot_p()
        return f, "FTPS"
    except Exception as ex:
        print("FTPS 失败（%s），改用普通 FTP" % ex)
        f = ftplib.FTP()
        f.connect(CFG["host"], CFG["port"], timeout=60)
        f.login(CFG["username"], CFG["password"])
        return f, "FTP"


def ensure_dir(f, path, seen):
    if path in seen:
        return
    cur = ""
    for part in [p for p in path.split("/") if p]:
        cur += "/" + part
        if cur in seen:
            continue
        try:
            f.mkd(cur)
        except ftplib.error_perm:
            pass
        seen.add(cur)


def remote_sizes(f, base):
    """递归列出 base 下现有文件大小，用来跳过没变的文件。"""
    sizes = {}

    def walk(d):
        try:
            for name, facts in f.mlsd(d, facts=["type", "size"]):
                p = d.rstrip("/") + "/" + name
                if facts.get("type") == "dir":
                    walk(p)
                elif facts.get("type") == "file":
                    sizes[p] = int(facts.get("size", -1))
        except ftplib.all_errors:
            pass
    walk(base)
    return sizes


def main():
    build.build()
    f, mode = connect()
    print("已连接（%s）%s" % (mode, f.getwelcome()[:60]))
    base = CFG["remotePath"]
    existing = remote_sizes(f, base) if "--changed" in sys.argv else {}
    seen, up, skip = set(), 0, 0
    for p in sorted(SITE.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(SITE).as_posix()
        remote = base.rstrip("/") + "/" + rel
        if existing.get(remote) == p.stat().st_size:
            skip += 1
            continue
        ensure_dir(f, remote.rsplit("/", 1)[0], seen)
        for attempt in range(3):
            try:
                with open(p, "rb") as fh:
                    f.storbinary("STOR " + remote, fh)
                break
            except ftplib.all_errors + (TimeoutError, OSError) as ex:
                print("重试 %s（%s）" % (rel, str(ex)[:70]))
                try:
                    f.close()
                except Exception:
                    pass
                f, _ = connect()
                d, n = remote.rsplit("/", 1)
                try:
                    f.delete("%s/.in.%s." % (d, n))  # 清理上次中断留下的临时文件
                except ftplib.all_errors:
                    pass
        else:
            raise SystemExit("上传失败：" + rel)
        up += 1
    f.quit()
    print("完成：上传 %d 个，跳过 %d 个（大小未变）" % (up, skip))


if __name__ == "__main__":
    main()
