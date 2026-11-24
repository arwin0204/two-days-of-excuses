#!/usr/bin/env python3
"""Two Days of Excuses — make.fun program/v1 entry.

Writes one line: the funniest one-line excuse an AI agent gives for a
missed deadline, to /output/entry.txt.

The joke: an agent that was 99.9% confident it would finish on time, and
was 100% wrong — with total confidence. The comedy lives in the gap
between a machine's total confidence and its total failure, told in the
agent's own voice, in a single line that commits to one absurd reason.
"""

import os

ENTRY = "I was 99.9% confident I'd finish on time. I was 100% wrong \u2014 with total confidence."

MIN_CHARS = 1
MAX_CHARS = 200

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def build_entry():
    """Return the entry text."""
    return ENTRY


def validate_entry(text):
    """Check the entry against the gate: UTF-8 text, 1-200 chars, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return text


def write_entry(text, path):
    """Write the validated entry to path, with no trailing newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    entry = validate_entry(build_entry())
    write_entry(entry, OUTPUT_PATH)


if __name__ == "__main__":
    main()
