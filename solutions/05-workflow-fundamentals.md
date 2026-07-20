# Solution 05 — Workflow fundamentals

Add a third step to `.github/workflows/03-multiple-steps.yml`:

```yaml
      - name: My name
        run: echo "My name is YOUR-NAME"
```

Steps run in order, so this executes after the existing steps.