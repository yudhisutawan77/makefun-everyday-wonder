"""Everyday Wonder, Two Days to Find the Line.

Entry: a single sentence (<=200 characters) that makes a small everyday
moment strange and new. The sentence lives in ENTRY and is printed to
stdout and written to the entry file when this script runs.
"""

import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


MAX_CHARS = 200


def validate_entry(text):
    """Check the entry is one sentence, non-empty, <=200 chars, UTF-8."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be a non-empty string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if not text.endswith("."):
        raise ValueError("entry must end with a single full stop")
    if text.count(".") != 1:
        raise ValueError("entry must contain exactly one sentence")
    text.encode("utf-8")
    return text


def entry_output_path():
    """Honour ENTRY_OUT, else ENTRY_OUT_DIR, else /output."""
    out = os.environ.get("ENTRY_OUT")
    if out:
        return out
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(text):
    path = entry_output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return path


ENTRY = (
    "The elevator mirror caught me mid-yawn, and for one floor I was "
    "a stranger politely pretending not to know me."
)


def main():
    entry = validate_entry(ENTRY)
    write_entry(entry)
    print(entry)


if __name__ == "__main__":
    main()
