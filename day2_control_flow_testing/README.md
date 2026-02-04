# Day 2 -- Control Flow & Testing

This day focuses on Python control flow fundamentals and introducing
testing with **pytest** through a practical task.

## What Was Covered

-   `if / elif / else`
-   Truthy vs Falsy values
-   Logical operators: `and`, `or`, `not`
-   Short-circuit behavior
-   Ternary expressions
-   Intro to `pytest`

## Project Structure

    day2_control_flow_testing/
    ├── bmi.py
    ├── test_bmi.py
    └── README.md

## BMI Calculator

-   Function: `bmi_calculator(height, weight)`
-   Uses metric units (meters, kilograms)
-   Returns BMI rounded to 2 decimals
-   Validates inputs and raises proper errors

## Testing

-   Written using `pytest`
-   Covers valid, invalid, and edge cases
-   All tests pass using `pytest -v`
