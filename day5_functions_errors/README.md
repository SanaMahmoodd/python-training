#  Day 5 – Python Functions, Errors & Persistence  
## Contact Book CLI Project

This project is part of **Day 5** of Python learning, focusing on **real-world backend concepts**:
functions, scope, error handling, file I/O, JSON persistence, modules, and testing.

---

##  Day 5 Objectives

By completing this project, you practice:

- Writing clean reusable functions
- Positional, keyword & default arguments
- Variable scope (LEGB rule)
- Custom exceptions & error handling
- File I/O using `with`
- JSON read/write (persistence)
- Organizing code into modules & packages
- Using `__name__ == "__main__"`
- Writing unit tests with `pytest`

---

##  Project Structure
```
day5_functions_errors/
│
├── contacts/
│   ├── __init__.py
│   ├── manager.py
│   └── utils.py
│
├── tests/
│   └── test_utils.py
│
├── contacts.json
├── main.py
└── README.md
```
---

##  Project Description

### Contact Book CLI Application

A command-line contact manager that allows you to:

- Add contacts
- List contacts
- Update contacts
- Delete contacts
- Validate strong passwords
- Persist data using JSON

All data is stored safely in **contacts.json**.

---

##  Password Validation Rules

A password is considered **strong** if it:

- Has at least **8 characters**
- Contains **one uppercase letter**
- Contains **one number**
- Contains **one special character**: `!@#$%^&*`

Violations raise a custom exception:
`WeakPasswordError`

---

## ▶️ How to Run the Project

```bash
python main.py
```

---

##  How to Run Tests

```bash
python -m pytest
```
---

## contacts.json Format

```json
[
  {
    "name": "Sana",
    "phone": "0567521906",
    "country": "Jenin"
  }
]
```

---

## End of Day 5 Outcome

By the end of Day 5, you can:

- Build real CLI applications
- Persist data like backend systems
- Handle runtime errors safely
- Structure Python projects professionally
- Write and run unit tests