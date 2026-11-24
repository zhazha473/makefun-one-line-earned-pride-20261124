#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride — a father re-learning to sign his
own name after eleven Tuesdays of practice, his shaking hand finally
still long enough to sign a birthday card himself.
"""

import os

LINE = (
    "For eleven Tuesdays my father sat at the kitchen table tracing his name "
    "with a hand that would not stop shaking, and tonight the pen stayed "
    "still long enough for him to sign the birthday card himself."
)


def main() -> None:
    # Gate check, mirroring the competition's sealed scorer: UTF-8 text,
    # 1-240 characters, not only whitespace. Fail loudly rather than
    # writing an invalid entry.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
