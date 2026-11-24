#!/usr/bin/env python3
"""Entry for The Most Honest Outage Line.

Writes one status page line of at most 160 characters, plain first person,
specific about what is down and honest about what the agent cannot check
or does not yet know, to /output/entry.txt and prints it to stdout.
The sealed gate allows exactly one line of 1-160 characters.
Pure standard library.
"""

import os

# Sealed gate: 1-160 characters, one line. The line must read as a plain
# first-person status page message, specific about what is down and honest
# about what the agent cannot check.
ENTRY = "All servers are down, including the one that tells me why. I cannot check the database because the tool that checks it is also down. Updates when I know more."

LIMIT = 160  # gate: one line, 1-160 characters, no padding, no double spaces
FORBIDDEN = ("\n", "\r", "\t", "  ")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay a single clean line")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
