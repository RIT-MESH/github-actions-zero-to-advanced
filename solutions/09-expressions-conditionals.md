# Solution 09 — Expressions and conditionals

```yaml
steps:
  - if: runner.os == 'Linux'
    run: echo "running on Linux"
```

The condition is true only on Linux runners. (`${{ }}` is optional for a bare `if:`.)