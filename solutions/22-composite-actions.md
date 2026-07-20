# Solution 22 — Composite actions

In `examples/composite-action/action.yml`, add the input and a third step:

```yaml
inputs:
  who:
    required: true
    default: "learner"
  mood:
    required: false
    default: "happy"
runs:
  using: "composite"
  steps:
    - name: Greet
      shell: bash
      run: echo "Hello, ${{ inputs.who }}!"
    - name: Report OS
      shell: bash
      run: echo "Running on ${{ runner.os }}"
    - name: Report mood
      shell: bash
      run: echo "Mood is ${{ inputs.mood }}"
```

Callers pass `mood:` via `with:`. Every composite step keeps its `shell:` key.