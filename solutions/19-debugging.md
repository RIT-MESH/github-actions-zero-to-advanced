# Solution 19 — Debugging

Example: a run failed with `file not found` because `actions/checkout` was missing. Root cause: the runner had no copy of the repo. Fix: add `- uses: actions/checkout@v4` as the first step.