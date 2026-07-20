#!/usr/bin/env python3
"""Validate all YAML and JSON files in the repo parse correctly."""
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not installed; installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyYAML"])
    import yaml

REPO = Path(__file__).resolve().parents[1]
errors = 0

for yfile in REPO.rglob("*.y*ml"):
    rel = yfile.relative_to(REPO)
    try:
        yaml.safe_load(yfile.read_text(encoding="utf-8"))
    except Exception as e:  # noqa
        print(f"YAML ERROR {rel}: {e}")
        errors += 1
    else:
        print(f"OK YAML {rel}")

for jfile in REPO.rglob("*.json"):
    rel = jfile.relative_to(REPO)
    try:
        json.loads(jfile.read_text(encoding="utf-8"))
    except Exception as e:  # noqa
        print(f"JSON ERROR {rel}: {e}")
        errors += 1
    else:
        print(f"OK JSON {rel}")

if errors:
    print(f"{errors} file(s) failed validation")
    sys.exit(1)
print("All YAML and JSON files valid.")
