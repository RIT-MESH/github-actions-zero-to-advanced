#!/usr/bin/env python3
"""Basic structural check of workflow files."""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyYAML"])
    import yaml

REPO = Path(__file__).resolve().parents[1]
WF_DIR = REPO / ".github" / "workflows"
errors = 0

# YAML parses the bare word 'on' as the boolean True key. Accept either.
ON_KEYS = ("on", True)

for wf in sorted(WF_DIR.glob("*.y*ml")):
    try:
        data = yaml.safe_load(wf.read_text(encoding="utf-8")) or {}
    except Exception as e:  # noqa
        print(f"PARSE ERROR {wf.name}: {e}")
        errors += 1
        continue
    if "name" not in data:
        print(f"WARN {wf.name}: no 'name' key")
    has_on = any(k in ON_KEYS for k in data.keys())
    if not has_on:
        print(f"ERROR {wf.name}: no 'on' trigger")
        errors += 1
    if "jobs" not in data or not data["jobs"]:
        print(f"ERROR {wf.name}: no jobs")
        errors += 1
        continue
    for jid, job in data["jobs"].items():
        if "runs-on" not in job and "uses" not in job:
            print(f"ERROR {wf.name}: job '{jid}' missing runs-on/uses")
            errors += 1
    print(f"OK {wf.name}")

if errors:
    print(f"{errors} workflow problem(s)")
    sys.exit(1)
print("All workflow files structurally valid.")