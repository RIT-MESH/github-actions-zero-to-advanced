# Solution 18 — Deployment simulation

```yaml
  deploy-dev:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying to DEV (simulated)"
  deploy-staging:
    needs: deploy-dev
    ...
```

`deploy-dev` runs after `build` with no `environment:`; staging depends on it.