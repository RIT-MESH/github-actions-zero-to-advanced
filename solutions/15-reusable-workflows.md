# Solution 15 — Reusable workflows

In `.github/workflows/12-reusable-build.yml`, add a second input:

```yaml
on:
  workflow_call:
    inputs:
      app-name:
        required: true
        type: string
      language:
        required: false
        default: python
        type: string
```

And in the step:

```yaml
- run: echo "Building ${{ inputs.app-name }} in ${{ inputs.language }}"
```

Callers pass `language:` via `with:`.