"""One Line, Big Laugh — entry program.

Writes a single funny line (<=200 chars) to /output/entry.txt.
The line: a smart speaker asked for something relaxing answers with
the least relaxing thing it knows — the listener's bank balance.
Setup promises calm; the punchline delivers anxiety. No title,
no setup, no explanation around it: the line lands on its own.
The line is 69 characters, well inside the 200-character cap.
"""

import os

LINE = "I asked Alexa for something relaxing. She read out my bank balance."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
