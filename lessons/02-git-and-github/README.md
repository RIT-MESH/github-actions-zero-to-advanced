# Lesson 02 — Git and GitHub for complete beginners

## What are Git and GitHub?

- **Git** is a program on your computer that tracks changes to files over time. It keeps a history so you can see what changed and go back if needed.
- **GitHub** is a website that stores your Git-tracked projects online and lets people collaborate.

Analogy: Git is your personal notebook where you write and tear out pages of changes. GitHub is the shared library where everyone puts their notebooks so others can read and copy them.

## Why do they exist?

Because software is changed constantly by many people. Without Git, you would never be sure which version is the latest. Without GitHub, sharing those versions would be manual and messy.

## Install Git

Download Git from <https://git-scm.com/downloads> and install it. Then open a terminal:

- **Windows:** use **PowerShell** or **Git Bash**.
- **macOS/Linux:** use the **Terminal**.

Check it works:

```powershell
git --version
```

```bash
git --version
```

Expected output (your version may differ):

```text
git version 2.55.0
```

If it fails: Git is not installed or not on your PATH. Reinstall and reopen the terminal.

## Make your first repository

Run these one line at a time.

```powershell
# Windows PowerShell
mkdir my-first-project
cd my-first-project
git init -b main
```

```bash
# macOS / Linux
mkdir my-first-project
cd my-first-project
git init -b main
```

- `mkdir` creates a folder.
- `cd` moves into that folder.
- `git init -b main` starts Git tracking in this folder, with a first branch named `main`.

Expected output:

```text
Initialized empty Git repository in .../my-first-project/.git/
```

## Add a file and commit

A **commit** is a saved snapshot of your files.

```powershell
# Windows PowerShell
"Hello Git" | Set-Content notes.txt
git add notes.txt
git commit -m "Add my first note"
```

```bash
# macOS / Linux
echo "Hello Git" > notes.txt
git add notes.txt
git commit -m "Add my first note"
```

- The first line creates `notes.txt` with the text `Hello Git`.
- `git add` tells Git to include `notes.txt` in the next snapshot.
- `git commit -m "..."` saves the snapshot with a short message.

Expected output (last line):

```text
[main (root-commit) ...] Add my first note
 1 file changed, 1 insertion(+)
 create mode 100644 notes.txt
```

## Connect to GitHub

1. Sign up at <https://github.com> (free).
2. Click **New repository**, name it `my-first-project`, leave it **Public**, click **Create repository**.
3. GitHub shows you commands like these (already pointing at your repo):

```bash
git remote add origin https://github.com/YOUR-USERNAME/my-first-project.git
git push -u origin main
```

- `git remote add origin ...` connects your local folder to the online repository (named `origin`).
- `git push -u origin main` uploads your `main` branch to GitHub.

Refresh the GitHub page: your `notes.txt` file is now online.

## Common mistakes

- **Forgetting `git add` before `git commit`.** The commit saves nothing new.
- **Wrong remote URL.** `git push` fails with `Repository not found`. Copy the exact URL from GitHub.
- **Not committing before pushing.** There is nothing to upload.

## Knowledge check

1. What is the difference between Git and GitHub?
2. What does `git commit` do?
3. What does `git push` do?

