#!/usr/bin/env python3
"""Write this bounty entry to /output/entry.txt.

The entry is one fixed line, at most 200 characters, about the dumbest
thing our own agent did today. The program writes exactly that line and
nothing else: no trailing newline, no extra output file, no dependence
on the working directory. The write is atomic -- the line goes to a
temporary file in the same directory first, then replaces the target --
so a reader never sees a half-written entry.
"""

import os

ENTRY = "The relay died three times before my agent wrote a single line of code \u2014 then it blamed my typing speed."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
