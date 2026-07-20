# Solution 07 — Jobs

```yaml
permissions:
  contents: read
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - run: echo "setup"
  verify:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - run: echo "verify after setup"
```

`needs: setup` makes `verify` wait for `setup` to succeed.