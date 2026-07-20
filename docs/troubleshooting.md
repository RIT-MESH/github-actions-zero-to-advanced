# Troubleshooting

## Quick decision tree

```text
Did the workflow run at all?
├── No  -> Check `on:` trigger and that the file is under .github/workflows/
└── Yes -> Did a job fail?
            ├── Job skipped -> Check `if:` / `needs:`
            └── Job failed  -> Open the failing step and read the last log lines
                              ├── "file not found"     -> add actions/checkout@v4
                              ├── "permission denied"  -> add the needed permission
                              ├── "module not found"   -> install dependencies first
                              ├── "secret is empty"    -> check secret name/scope
                              └── YAML parse error      -> fix indentation (2 spaces)
```

## Common problems

### The workflow did not run

- Confirm the file is in `.github/workflows/` (plural).
- Confirm `on:` lists the event you triggered.
- For manual runs, confirm `workflow_dispatch` is present.

### "file not found" in tests

The runner is empty until you check out code. Make the first step:

```yaml
- uses: actions/checkout@v4
```

### Permission denied (releases, PRs)

Add the minimum permission:

```yaml
permissions:
  contents: write
```

### Tests fail: "No module named pytest" / "npm: not found"

Install dependencies before testing. See [`getting-started.md`](getting-started.md).

### Secret shows empty

- Confirm the secret name matches exactly (case-sensitive).
- If using an environment secret, confirm the job uses `environment:` with that environment name.

### Matrix job fails on one version

That Python version may be unavailable on the runner image. Use supported versions.

### Enabling debug logging

Add repo secrets `ACTIONS_RUNNER_DEBUG=true` and `ACTIONS_STEP_DEBUG=true`, then re-run.
