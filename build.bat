python anm2parser\run.py docs
del /S docs\index.html
copy anm2player\preview.html docs\index.html
npx tsc -p anm2player && python huijianmplayer/merge.py huijianmplayer/anm2player.js docs/player.js
