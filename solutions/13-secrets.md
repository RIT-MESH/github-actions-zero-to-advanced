# Solution 13 — Secrets

Store a repository secret `FAKE_TOKEN` with value `EXAMPLE_SECRET_VALUE`.

```yaml
env:
  FAKE_TOKEN: ${{ secrets.FAKE_TOKEN }}
steps:
  - run: echo "length is ${#FAKE_TOKEN}"
```

We print the length, never the value.