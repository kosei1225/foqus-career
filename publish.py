# -*- coding: utf-8 -*-
"""紹介サイト（テスト版）を GitHub Pages 用に組み立てる。
元：~/01_自分の事業_FOQUS/02_キャリア経営教材/キャリア経営教材/08_紹介サイト_テスト版/index.html（Artifact 用。doctype・head なし。2026-11-08 のフォルダ整理で ~/仕事/04_FOQUS/… から移動）
ここに index.html（doctype・charset・viewport・noindex を足したもの）と、index.html が使う画像だけを img/ に置く。
使い方：python3 publish.py → git add -A → git commit → git push（数十秒で https://kosei1225.github.io/foqus-career/ に反映）"""
import os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/01_自分の事業_FOQUS/02_キャリア経営教材/キャリア経営教材/08_紹介サイト_テスト版")

L = open(os.path.join(SRC, "index.html"), encoding="utf-8").read().split("\n")
end_style = next(i for i, l in enumerate(L) if l.strip() == "</style>")
head = [l for l in L[:end_style + 1] if "claude:viewport-fit-sides" not in l]
body = L[end_style + 1:]
html = ["<!doctype html>", '<html lang="ja">', "<head>", '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<meta name="robots" content="noindex, nofollow">'] + head + ["</head>", "<body>"] + body + ["</body>", "</html>", ""]
text = "\n".join(html)
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(text)

used = sorted(set(re.findall(r'img/[^"\'\s)]+', text)))
img = os.path.join(HERE, "img")
shutil.rmtree(img, ignore_errors=True); os.makedirs(img)
for u in used:
    shutil.copy(os.path.join(SRC, u), os.path.join(HERE, u))
print("index.html と画像", len(used), "枚を用意しました")
