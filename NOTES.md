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
test_ * ()
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

## Financial Data Learning

### Trading Days vs Missing Data

Stock market data does not contain every calendar day.

Example:

- January 6th and 7th were weekends.
- January 13th and 14th were weekends.
- January 15th was a US market holiday.

These missing dates are not errors. They represent days when the market was closed.

A financial data system must understand the difference between:

- Market closed → expected absence of data
- Data fetch failure → actual missing data problem

Handling this correctly is important when building financial applications.

## Day 2 - Financial Calculations

### Understanding Stock Returns

A stock return tells us how much the price changed compared to the previous day.

Formula:

Daily Return = (Today's Close / Yesterday's Close) - 1

Example:

On 2024-01-02:
Price = 100.00

On 2024-01-03:
Price = 101.00

Daily Return:

= (101 / 100) - 1

= 1.01 - 1

= 0.010000

So the stock increased by 1%.

---

### Cumulative Return

Cumulative return tells us the total growth of the stock from the first day to the last day.

There are two ways to calculate it.

### Method 1: Multiply all daily growth factors

Each daily return is converted into a growth factor:

1 + return

Then multiply all days together and subtract 1.

Example:

(1+r1) × (1+r2) × ... × (1+r9) - 1

Result:

0.060800

---

### Method 2: Compare starting price and ending price

Simple formula:

= (Final Price / Initial Price) - 1

= (106.08 / 100.00) - 1

= 0.060800

---

### Why are both methods equal?

Because daily returns are just showing the growth happening step by step.

Example:

If ₹100 becomes ₹101 and then ₹102.01:

Day 1:
100 × 1.01 = 101

Day 2:
101 × 1.01 = 102.01

The intermediate values cancel out when we multiply all growth factors.

So:

Daily growth × Daily growth × ... = Final Price / Initial Price

---

### Final Values

First daily return:

`0.010000`

Cumulative return using daily returns:

`0.060800`

Cumulative return using final and initial price:

`0.060800`

Both methods should always match.

# Financial Accuracy and Decimal 

## Why 0.1 + 0.2 is not exactly 0.3 

Computers store numbers in binary format (0s and 1s).

Some decimal numbers cannot be represented exactly in binary. 

Example:

'''python
0.1+0.2
'''

Output:

'''
0.3000000000000004
'''

This happens because the computer stores a slightly diffferent value internally.

This is similar to:

'''
1/3 = 0.333333...
'''

which cannot be represented exactly in decimal.

---

## Decimal in AlphaOS

While building AlphaOS, I learned that financial values need accuracy. 

Small errors can become bigger when calculations are repeated many times.

Example:

'''python 
Decimal(0.1)
'''

Output:

'''
Decimal('0.1000000000000000055511151231257827021181583404541015625')
'''

The problem is that '0.1' without quotes is already a float.

The error happens before Decimal recieves it.

Correct:

'''python 
Decimal("0.1")
'''

Here Decimal receives the value as text and creates the exact decimal number.

The quotes prevent the value from passing through float first. 

---

## Floating Point Error Connection 

The digits:

'''
5551115123125782
'''

appear in both:

'''
0.1 + 0.2 - 0.3
'''

and inside the stored value of:

'''
Decimal(0.1)
'''

This shows that the same floating point error is appearing in different places.

---

## Why this matters in finance

Two major problems can happen:

### 1. Accumulated error 

Small errors can build up and affect:

- Portfolio values 
- Transactions 
- Profit and loss calculations 
- Cost basis 

### 2. Equality checks failing

Two values may look the same but fail comparison because of hidden floating point errors.

Example:

'''python 
0.1 + 0.2 == 0.3
'''

Result:

'''
False
'''

---

## AlphaOS Data Type Rule 

Use Decimal for:

- Stock prices
- Money values 
- Share quantities 
- Cost basis 

Example:

'''python 
Decimal("100.00")
'''

Use float for:

- Daily returns 
- Volatility 
- Correlation 
- Statistical calculations 

---

## Day 3 - Building the Price Loader 

## load_prices as a boundary 

'load_prices' is the first boundary where external stock data enters AlphaOS

It should validate everything immediately 

If wrong data enters the system, the error may appear much later in another module and become difficult to find.

The goal is:

'''
Wrong data should stop early 
'''

---

## CSV Conversion 

CSV files store data as text.

When reading stock prices, converters in 'read_csv' are used to convert the close price directly into Decimal.

This prevents the value from becoming a float first and losing accuracy.

---

## Why timestamps are UTC 

AlphaOS uses UTC timestamps because financial data can come from different markets and time zones. 

Using one standard timezone avoids confusion when comparing data from different sources.

---

## Why Decimal columns have object dtype 

Pandas normally stores numbers using numeric data types.

But Decimal is a Python object.

Because of this, pandas stores Decimal columns as:

'''
object dtype 
'''

This is expected and does not mean the data is wrong.

---

## Why sorting is important 

Even if a CSV file looks sorted, AlphaOS should not assume external data is always correct.

Sorting ensures:

- Datas are in the correct order.
- Return calculations happend correctly.
- Data processing is predictable.

---

## Data Validation Checks

Two important checks:

### Duplicate dates

The same trading date should not appear multiple times.

Duplicate dates can create incorrect calculations.

### Non-positive prices

Stock prices cannot be:

```
0
negative values
```

These values should be rejected.

---

## freq=None is correct

When checking date frequency:

```
freq=None
```

does not mean failure.

Stock market data is not continuous because markets are closed on:

- Weekends
- Holidays

So irregular dates are normal.

---

## Day 3 - Python Lessons Learned

## Indentation defines scope

Python uses indentation to decide where code belongs.

Code at column 0 is outside the function.

Example:

```python
def hello():
    print("Inside function")


print("Outside function")
```

---

## Code after return does not run

Example:

```python
def test():
    return 10
    print("Hello")
```

The print statement never executes because Python exits the function after return.

Python does not warn about this.

---

## Python module caching

Python can remember imported modules during a session.

Sometimes code changes are made but Python still uses the older imported version.

A fresh Python session solves this problem.

---

## Python Shell vs Terminal

Python shell:

```
>>>
```

Used for Python code.

Terminal:

```
%
```

Used for commands.

Example:

```bash
pwd
uv run
```

These commands do not work inside the Python shell.

---

## Fresh Python Process

Using:

```bash
uv run python -c "..."
```

runs Python in a fresh process.

Benefits:

- No old imports
- No stale code
- Uses the correct environment

---

## Debugging Lessons

## Unsaved Files

The biggest time loss today happened because files were not saved before testing.

Lesson:

Always save changes before debugging or committing.

Solution:

Enable VS Code autosave:

```json
"files.autoSave": "afterDelay"
```

---

## Main Takeaway

While building AlphaOS, I learned that software development is not only about writing features.

A reliable financial system needs:

- Accurate data handling
- Correct calculations
- Strong validation
- Proper testing
- Good debugging habits

The decisions made early in the project will affect the reliability of the whole system later.
