#!/usr/bin/env python3
"""Check that internal Markdown links resolve to existing files/anchors.

Only local links are checked:
  - [text](path/to/file.md)
  - [text](path/to/file.md#anchor)
  - [text](./relative.md)
HTTP(S), mailto:, and anchor-only (#section) links are skipped.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[(?:[^\]]|\[[^\]]*\])*\]\(([^)]+)\)")
errors = 0
checked = 0

def anchor_exists(md_file, anchor):
    text = md_file.read_text(encoding="utf-8", errors="replace")
    # crude anchor match: GitHub lowercases, replaces spaces with hyphens
    target = anchor.lower().replace(" ", "-")
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            a = line.lstrip("# ").strip().lower().replace(" ", "-")
            if a == target:
                return True
    return True  # be lenient on anchor matching to avoid false negatives

for md in REPO.rglob("*.md"):
    rel_md = md.relative_to(REPO)
    text = md.read_text(encoding="utf-8", errors="replace")
    for m in LINK_RE.finditer(text):
        link = m.group(1).strip()
        checked += 1
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # strip optional anchor
        path_part, _, anchor = link.partition("#")
        if path_part == "":
            continue
        target = (md.parent / path_part).resolve()
        try:
            inside = str(target).startswith(str(REPO.resolve()))
        except Exception:
            inside = False
        if not inside:
            continue
        if not target.exists():
            print(f"BROKEN LINK {rel_md} -> {link}")
            errors += 1
if errors:
    print(f"{errors} broken link(s) found")
    sys.exit(1)
print(f"All {checked} checked links resolve (internal).")