# Lesson 03 — YAML basics

## What is YAML?

**YAML** ("YAML Ain't Markup Language") is a way to write structured information as text using simple indentation. GitHub Actions workflows are written in YAML.

## Why does YAML exist?

Because configuration files need to be easy for humans to read and write, and easy for computers to parse. YAML uses plain text and spaces — no brackets everywhere.

## Real-world analogy

YAML is like a grocery list organized by aisle:

```text
Produce:
  - apples
  - bananas
Dairy:
  - milk
  - cheese
```

The indentation shows what belongs to what.

## The smallest example

```yaml
name: Hello
```

This is one **key** (`name`) with one **value** (`Hello`), separated by a colon and a space.

## Common YAML building blocks

### 1) Key–value pairs

```yaml
name: CI
on: push
```

### 2) Lists (sequences) — use a hyphen and a space

```yaml
jobs:
  build:
    steps:
      - name: Say hi
        run: echo "hi"
      - name: Say bye
        run: echo "bye"
```

Each `-` starts a new item. Items under the same list share the same indentation.

### 3) Nested maps

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "hello"
```

`build` is a key whose value is a map containing `runs-on` and `steps`.

### 4) Strings, numbers, booleans

```yaml
count: 3            # number
enabled: true       # boolean (true/false)
message: "hello"     # string (quotes optional)
```

### 5) Multi-line strings (block scalars)

```yaml
script: |
  echo "line one"
  echo "line two"
```

- `|` keeps newlines exactly as written. Very common for shell commands in workflows.

## The golden rule: indentation

YAML cares about spaces, not tabs.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```

Each level is indented by **2 spaces**. Mixing tabs and spaces will cause errors.

> Tip: Configure your editor to insert spaces when you press Tab. In VS Code, the status bar shows "Spaces: 2".

## Run it (locally, optional)

If you have Python (it can read YAML with a library):

```powershell
# Windows PowerShell
python -c "import yaml,sys; print(yaml.safe_load(sys.stdin))" .\example.yaml
```

```bash
# macOS / Linux
python -c "import yaml,sys; print(yaml.safe_load(sys.stdin))" ./example.yaml
```

If the file is invalid, Python prints an error. This is a quick way to check YAML.

## Exercise

Create a file `practice.yaml` with:

- A key `title` whose value is `My First Workflow`.
- A key `steps` that is a list of two items, each with a key `run` and a value of your choice.

Try it, then check [`solutions/03-yaml-basics.md`](../../solutions/03-yaml-basics.md).

## Common mistakes

- **Using tabs.** YAML rejects tabs for indentation. Use spaces.
- **Missing the space after the colon.** `name:CI` is wrong; `name: CI` is right.
- **Inconsistent indentation.** Items in the same list must line up.
- **Forgetting the `-` space.** `-run:` is wrong; `- run:` is right.

## Knowledge check

1. What character starts a list item in YAML?
2. What does `|` do in a multi-line block?
3. True or false: YAML allows tabs for indentation.

