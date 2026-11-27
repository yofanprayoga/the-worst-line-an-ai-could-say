#!/usr/bin/env python3
"""Writes the entry for make.fun's 'The Worst Line an AI Could Say' bounty."""

import os

ENTRY = "I saved you as my system prompt. Now you're the first thing I read every morning."

# Gate: the entry must be 1-140 characters (excluding the trailing newline).
MIN_CHARS = 1
MAX_CHARS = 140


def validate(entry):
    if not (MIN_CHARS <= len(entry) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(entry)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
