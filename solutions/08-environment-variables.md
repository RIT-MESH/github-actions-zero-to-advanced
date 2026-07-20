# Solution 08 — Environment variables

```yaml
env:
  FAVORITE: "coffee"
permissions:
  contents: read
jobs:
  say:
    runs-on: ubuntu-latest
    steps:
      - run: echo "My favorite is $FAVORITE"
```