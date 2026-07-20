# Solution 11 — Artifacts and caching

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: readme-snapshot
    path: README.md
```

The file appears under the run's Artifacts on the Actions tab.