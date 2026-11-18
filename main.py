# news-image-20261117 entry (Python 3.13, standard library only).
#
# The entry is the image in entry.png beside this file: a newspaper front
# page summing up the world's news of Tuesday 17 November 2026, drawn and
# composed in the build session that produced this repository. This program
# simply copies that image to the grader's output directory, so both runs
# write byte-identical output.
#
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUTPUT_DIR / "entry.png")
