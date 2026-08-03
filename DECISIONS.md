# Decisions 

## 2026-08-03 - mypy and pandas type checking 

### Decision 

I decided to ignore missing pandas type information in mypy for now.

Added:

'ignore_missing_imports = true'

for pandas in 'pyproject.toml'.

### Why I chose this 

I considered installing 'pandas-stubs' for better type checking.

But right now, my project uses only basic pandas features, and strict checking creates many extra errors inside pandas itself 

Those errors do not help me improve my own code at this stage 

So for now:
- My own code will still be checked by mypy 
- Pandas internal code will be ignored

### Revisit 

I will review this decision in Week 2 when AlphaOS starts using pandas more heavily 