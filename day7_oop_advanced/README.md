# Day 7 - OOP Advanced

## Overview
This task covers advanced Object-Oriented Programming (OOP) concepts in Python.

Implemented concepts:

- Inheritance
- Method overriding
- `super()`
- Encapsulation (private variables: `_var`, `__var`)
- Composition vs Inheritance

---

## Project Structure

```
day7_oop_advanced/
│
├── models.py
├── test_models.py
└── README.md
```

---

## Classes Implemented

### 1) Student
- Base class representing a student.
- Uses encapsulation with a private grades list (`__grades`).
- Methods:
  - `add_grade()`
  - `get_average()`
  - `get_grades()`
  - `__str__()`

### 2) GraduateStudent (Inheritance)
- Inherits from `Student`.
- Adds:
  - `thesis_title`
- Uses `super()` to call parent constructor.
- Overrides `__str__()` (method overriding).

### 3) Professor
- Can assign grades to students.
- Method:
  - `assign_grade(student, grade)`

### 4) Course (Composition)
- A course **contains** students (composition).
- Methods:
  - `enroll()`
  - `drop()`
  - `class_average()`

---

## Testing

Tests are written using **pytest** and cover:

- Student grading and average
- Encapsulation behavior
- Inheritance and overridden methods
- Professor assigning grades
- Course composition and class average

Run tests:

```bash
python -m pytest
```

---

## Learning Outcomes

By completing this task, you practice:

- Designing class hierarchies using inheritance
- Using `super()` correctly
- Applying encapsulation principles
- Understanding composition vs inheritance
- Writing clean OOP code with tests
