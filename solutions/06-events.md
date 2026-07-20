# Solution 06 — Events

```yaml
name: Dev + Manual
on:
  push:
    branches: [dev]
  workflow_dispatch:
permissions:
  contents: read
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - run: echo "ran"
```

`workflow_dispatch` adds the manual Run button; `push` to `dev` auto-triggers it.