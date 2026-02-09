# Day 4 – Data Structures (Deep Dive)
## CLI Contact Book

This project is part of the Python training program (Day 4).
It focuses on practicing core Python data structures through a
command-line **Contact Book** application.

---

## 📌 Topics Covered

- Lists (iteration, sorting)
- Tuples (conceptual understanding)
- Dictionaries (dict of dicts)
- Sets (used for tags)
- Loop-based CLI programs
- Safe data access using `.get()`
- Basic time complexity analysis

---

## 🗂 Project Structure

day4_data_structures/
├── contact_book.py
└── README.md

---

## ▶️ How to Run

1. Activate your virtual environment.
2. Navigate to the Day 4 folder:
```
cd day4_data_structures
```
3. Run the program:
```
python contact_book.py
```

---

## 🧠 Data Structure Design

Contacts are stored using a dictionary of dictionaries:

contacts = {
    "Ali Ahmad": {
        "phone": "0599...",
        "email": "ali@email.com",
        "tags": {"work", "gym"}
    }
}

- Main key: contact name
- phone / email: strings
- tags: set (unique values)

---

## ✨ Features

- Add a new contact
- Prevent duplicate names (with overwrite confirmation)
- Search by name (exact match)
- Search by phone number
- List all contacts sorted by name
- Delete contact by name
- Friendly output messages

---

## ⏱ Time Complexity Analysis

- Add contact (check duplicate): O(1) average
- Search by name: O(1) average
- Search by phone: O(n)
- Delete contact: O(1) average
- List contacts:
  - Iteration: O(n)
  - Sorting: O(n log n)

---

## 📝 Notes

- This project is for learning purposes.
- Uses only concepts covered up to Day 4.
- Code prioritizes clarity and readability.

---

✅ End of Day 4