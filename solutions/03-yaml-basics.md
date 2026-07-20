# Solution 03 — YAML basics

```yaml
title: My First Workflow
steps:
  - run: echo "step one"
  - run: echo "step two"
```

`title` is a key with a string value. `steps` is a list of two items; each item is a map with a `run` key. Indentation is 2 spaces per level.