# Solution 16 — Releases

```yaml
permissions:
  contents: write
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - run: echo "v0.2.0 notes" > notes.txt
      - uses: softprops/action-gh-release@v2
        with:
          tag_name: v0.2.0
          name: Release v0.2.0
          files: notes.txt
```

Requires `contents: write` and pushing tag `v0.2.0` (or using `workflow_dispatch`).