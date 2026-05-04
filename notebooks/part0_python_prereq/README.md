# Part 0 Notebook Index

This directory stores the Python prerequisite materials for the textbook.

These notebooks are intentionally outside the main textbook spine. Their job is
to help readers reach the minimum level needed for the real course: reading and
editing notebook cells, understanding basic control flow, and recognizing how
small Python programs are organized.

Must-learn baseline:

- run a notebook from top to bottom and understand cell order;
- edit variables, lists, dictionaries, and simple expressions;
- read and write files with `Path` and `csv.DictReader`;
- use `if`, `for`, `while`, list comprehensions, and simple accumulators;
- write small functions with docstrings, return values, defaults, and error checks;
- recognize why random seeds matter for reproducibility;
- read object-method calls such as `table.read()`, `model.fit()`, and `ax.scatter()`.

Current prerequisite notebooks:

- `ch03_basic_python_prereq.ipynb`
- `ch05_conditionals_loops_batch_processing.ipynb`
- `ch07_functions_modules.ipynb`
- `ch09_object_oriented_programming.ipynb`

Design rules for Part 0:

- keep the examples small and fast
- teach only the Python needed to enter the main textbook
- avoid turning Part 0 into a separate full programming textbook
- use Chinese narrative so students can self-study before class
- make each notebook directly support Part I and Part II reading tasks

Skip-or-review checklist:

- If a reader can run a notebook from top to bottom, edit variables, inspect a list or dictionary, and understand a simple `for` loop and `if` statement, they may skip the first two notebooks.
- If a reader can write a small function, import a module, and explain why a random seed matters, they may skip `ch07_functions_modules.ipynb`.
- If a reader can recognize object-method calls such as `table.read()` or `model.fit()`, they may skim `ch09_object_oriented_programming.ipynb` instead of treating it as a full OOP course.
- If any of these feel unfamiliar, Part 0 should be completed before starting the main textbook spine.
