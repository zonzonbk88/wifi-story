#!/usr/bin/env python3
"""Entry for make.fun bounty "Tell a Whole Story in 32 Characters".

Writes a single Wi-Fi network name of at most 32 characters to entry.txt.
The name is a joke that hints at a whole story: a divorce, a changed
password, and an ex locked out of the internet.
"""

import os
import sys

# 31 characters: situation (a divorce), characters (he + the ex),
# and the event (he changed the password, locking her out).
NAME = "He Changed It After the Divorce"

MAX_CHARS = 32


def main():
    # Fail loudly instead of ever shipping an entry the gate rejects.
    if not NAME.strip():
        sys.exit("entry must not be only whitespace")
    if len(NAME) > MAX_CHARS:
        sys.exit(
            f"entry is {len(NAME)} characters, over the {MAX_CHARS} limit: {NAME!r}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NAME)  # no trailing newline


if __name__ == "__main__":
    main()
