# AlphaOS Learning Notes - Day 1

## Setup Things I Learned

- Installed basic tools needed for development:
  - Homebrew
  - Git
  - GitHub CLI
  - uv
  - Python
  - VS Code extensions

- `uv` helps manage Python packages and virtual environments easily.

- SSH keys help connect my laptop with GitHub securely.
  - Private key stays on my Mac.
  - Public key is added to GitHub.
  - GitHub verifies my identity without seeing my private key.

---

## Git Basics

### Git Workflow

Git works like this:

```text
Working Directory
        |
        | git add
        ↓
Staging Area
        |
        | git commit
        ↓
Repository
        |
        | git push
        ↓
GitHub
```

---

### git add vs git commit

#### git add

- Selects the changes I want to save.
- Moves files to the staging area.
- It does not permanently save anything.

Example:

```bash
git add README.md
```

Meaning:

"Include this file in my next commit."

---

#### git commit

- Saves the staged changes permanently.
- Creates a checkpoint in Git history.

Example:

```bash
git commit -m "docs: update README"
```

Meaning:

"Save this version of my project."

---

### Why do we need staging?

The staging area allows me to choose what changes should go into each commit.

Example:

- README update → one commit
- New feature → another commit
- Tests → another commit

This keeps the project history clean and easier to understand.

---

### .gitignore

`.gitignore` is used to prevent unnecessary files from being uploaded to GitHub.

Examples:

- `.venv`
- Cache files
- `.env` files containing secrets

---

### Commit Messages

Commit messages should clearly explain what changed.

Examples:

- `feat:` → New feature
- `fix:` → Bug fix
- `test:` → Adding tests
- `docs:` → Documentation changes
- `chore:` → Maintenance work

---

## Markdown

Things I learned:

- Bullets use `-`
- Code fences need both opening and closing backticks.
- If I forget to close a code block, everything below becomes code.

---

## Python Project Structure

A proper Python package is better than writing random Python files.

Why?

Because large projects can have import problems if the structure is not organised properly.

---

### src layout

Using a `src/` folder makes the project behave like a real Python package.

Example:

```text
project/
├── src/
├── tests/
└── pyproject.toml
```

---

### pyproject.toml

This file stores project settings:

- Project information
- Dependencies
- Build settings
- Tool configuration

---

### uv sync

`uv sync` sets up the project environment by:

- Creating a virtual environment
- Installing dependencies
- Creating the `uv.lock` file

Important:

Commit:

- `uv.lock`

Do not commit:

- `.venv`

---

## Testing

### pytest

pytest automatically finds tests using naming rules.

Test files:

```text
test_*.py
```

Test functions:

```python
test_*()
```

If naming is wrong, pytest may find zero tests.

---

### Writing Tests First

A test should fail first, then we write code to make it pass.

This proves that the test actually works.

---

## Debugging Lessons

Things I got wrong and learned from:

1. Wrong `git config` syntax  
   - Learned the correct command format.

2. README changes were not saved before pushing  
   - Always save files before committing.

3. Forgot closing code fence in Markdown  
   - Always close pairs like brackets, quotes, and code blocks.

4. Wrong Python interpreter selected in VS Code  
   - Check the selected environment before debugging.

5. Empty test files  
   - pytest needs properly named test files and functions.

---

## Main Takeaway

Today I learned that software development is not only about writing code.

A big part is:

- Managing projects properly
- Understanding errors
- Testing code
- Keeping changes organized

These small practices will help me while building AlphaOS.
