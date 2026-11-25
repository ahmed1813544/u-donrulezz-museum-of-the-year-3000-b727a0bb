"""Museum of the Year 3000 - entry program.

Writes a single-line museum label to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).

Deterministic: the same label is written on every run.
"""

import os

LABEL = "Do Not Disturb sign, c. 2024. A paper talisman hung on a door to repel strangers; it worked by magic, as no one ever knocked."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
