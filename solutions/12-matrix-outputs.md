# Solution 12 — Matrix and outputs

```yaml
strategy:
  matrix:
    python-version: ["3.10", "3.11", "3.12", "3.13"]
```

Four jobs run, one per version. If a version is unavailable on the runner image, that job fails — pick supported versions.