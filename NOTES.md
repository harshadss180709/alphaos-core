# AlphaOS Learning Notes

## 1. Git Basics

### What is Git?

Git is a version control system used to track changes in a project.

It helps developers:

- Save different versions of code
- Track what changes were made
- Go back to previous versions if something breaks
- Work safely on large projects

---

# Git Workflow

```
Working Directory
        |
        | git add
        ↓
Staging Area
        |
        | git commit
        ↓
Git Repository
        |
        | git push
        ↓
GitHub Repository
```

---

# git add

## Meaning:

`git add` selects the changes that we want to save.

It moves files from:

**Working Directory → Staging Area**

Example:

```bash
git add README.md
```

Meaning:

"Git, include this file in my next save."

Important:

- It does not permanently save anything.
- It only prepares the changes for a commit.

---

# git commit

## Meaning:

`git commit` permanently saves the selected changes in Git history.

Example:

```bash
git commit -m "docs: update README"
```

Meaning:

"Save this version of my project with this message."

A commit creates a checkpoint that we can return to later.

---

# Why do we need both git add and git commit?

Git separates these steps because we may change multiple files but want to save them separately.

Example:

Changes made:

```
README.md       → Documentation update
app.py          → New feature
test.py         → Testing
```

Instead of saving everything together, we can choose:

Commit 1:

```
README update
```

Commit 2:

```
Added new feature
```

Commit 3:

```
Added tests
```

This keeps project history clean and easier to understand.

---

# Simple Real-Life Example

Think about submitting an assignment:

Working Directory:

- Your unfinished assignment

git add:

- Selecting the pages you want to submit

Staging Area:

- Pages ready for submission

git commit:

- Final submission with a title

git push:

- Uploading it to GitHub

---

# Important Commands

Check changed files:

```bash
git status
```

Add a file:

```bash
git add filename
```

Save changes:

```bash
git commit -m "message"
```

Upload to GitHub:

```bash
git push
```

---

# Key Remember Point

`git add` = Select changes

`git commit` = Save changes permanently

`git push` = Upload saved changes to GitHub
