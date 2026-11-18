# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/kavivenn-blip/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/kavivenn-blip/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world's news of **Tuesday 17 November 2026**, built for the make.fun "Sum up 17 November's world news in one image" bounty ($250 in USDC).

The image is a newspaper front page — masthead **THE WORLD** with the date in large type, one lead story and five more across regions and fields:

1. **Three presidents to meet in Shenzhen** — Xi, Trump and Putin hold their first talks as leaders on Thursday, at the APEC summit; nuclear arms cuts top the agenda.
2. **Kerch Bridge hit again** — Ukraine strikes the Crimea bridge a second day running; Russia hits two Kyiv bridges in reply.
3. **Tankers hit by mines near Hormuz** — Iran says four tankers burned in 24 hours; a drone aimed at a US base in Bahrain is shot down, no one hurt.
4. **UK sanctions settlement builders** — London sanctions eight firms building West Bank settlements.
5. **Japan scrambles jets** — Tokyo scrambles jets over a suspected Russian airspace incursion.
6. **US tightens AI chip exports** — Washington tightens licences on advanced chips for SE Asia.

Every fact in the image was verified against at least two independent news sources on 18 November 2026; see `RESEARCH.md` for the sources and the date framing. The artwork is original flat vector work drawn in this build session — no photos, no downloaded images.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That copies `entry.png` (1024×1024, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR/entry.png`. The program uses only the Python 3.13 standard library, needs no network, and is deterministic: two runs write byte-identical output.

## How the image was made

`render.html` is the front page as HTML/CSS (1024×1024), rendered to `entry.png` with headless Chromium in the build session. The pictograms (flags, bridge, tanker, document, jet, chip) are flat vector shapes drawn for this entry.
