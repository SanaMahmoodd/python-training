# Day 3 -- Iteration, Comprehensions & Built-ins

This day focuses on practicing Python iteration, using built-in
functions, and writing simple, clean logic with tests.

------------------------------------------------------------------------

## Topics Covered

-   Iteration using `for` and `while`
-   `break`, `continue`, and `else` with loops
-   List and dictionary comprehensions
-   Built-in functions:
    -   `sorted`
    -   `map`
    -   `filter`
    -   `zip`
    -   `enumerate`
    -   `any` / `all`
-   Understanding the difference between loops, comprehensions, and
    built-ins

------------------------------------------------------------------------

## Project Structure

    day3_iteration_comprehensions/
    ├── grades.py
    ├── test_grades.py
    └── README.md

------------------------------------------------------------------------

## Hands-on Task: Grades Processing

### Description

A simple program that: 
- Stores students and their grades 
- Returns the top 3 students based on grades 
- Converts grades into pass/fail results 
- Validates input data before processing

### Key Functions

-   `top_three_students(students)`
-   `pass_fail(students)`

------------------------------------------------------------------------

## ▶️ How to Run the Code

To run the examples in this folder:

1. Activate the virtual environment:
```bash
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS / Linux
```

2. Navigate to the Day 3 folder:
```bash
cd day3_iteration_comprehensions
```

3. Run the script:
```bash
python grades.py
```
------------------------------------------------------------------------

## Testing

-   Tests are written using `pytest`
-   Covers basic valid and invalid cases
-   Ensures sorting and validation work correctly

Run tests using:

``` bash
pytest -v
```

------------------------------------------------------------------------

## Outcome

By the end of Day 3, I gained better understanding of iteration, Python
built-ins, and writing readable, testable code.