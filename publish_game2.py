# -*- coding: utf-8 -*-
"""経営ゲーム「わたし株式会社」試作2「週末の焼き菓子」を GitHub Pages 用に置く。
元：~/01_自分の事業_FOQUS/02_キャリア経営教材/キャリア経営教材/04_ゲーム_わたし株式会社/試作2_週末の焼き菓子/index.html（そのまま開いて遊べる版。noindex つき）
ここに game2/index.html として写す。使い方：python3 publish_game2.py → git add -A → git commit → git push
（数十秒で https://kosei1225.github.io/foqus-career/game2/ に反映）"""
import os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/01_自分の事業_FOQUS/02_キャリア経営教材/キャリア経営教材/04_ゲーム_わたし株式会社/試作2_週末の焼き菓子/index.html")
t = open(SRC, encoding="utf-8").read()
assert 'name="robots" content="noindex' in t, "noindex がない"
os.makedirs(os.path.join(HERE, "game2"), exist_ok=True)
shutil.copy(SRC, os.path.join(HERE, "game2", "index.html"))
print("game2/index.html を置きました", len(t.encode("utf-8")), "bytes")
