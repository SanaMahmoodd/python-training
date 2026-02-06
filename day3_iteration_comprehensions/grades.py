def validate_students(students):
    if type(students) is not dict:
        raise TypeError("students must be a dictionary")

    for name in students:
        grade = students[name]

        if type(name) is not str:
            raise TypeError("student name must be a string")

        if type(grade) not in (int, float):
            raise TypeError("grade must be a number")

        if grade < 0 or grade > 100:
            raise ValueError("grade must be between 0 and 100")


def top_three_students(students):
    validate_students(students)

    sorted_students = sorted(
        students.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_students[:3]


def pass_fail(students):
    validate_students(students)

    return {
        name: "pass" if students[name] >= 50 else "fail"
        for name in students
    }

if __name__ == "__main__":
    students = {
        "Ali": 85,
        "Sana": 92,
        "Omar": 74,
        "Ruaa": 48,
        "Jana": 66
    }

    print("Top 3 students:")
    print(top_three_students(students))

    print("\nPass / Fail results:")
    print(pass_fail(students))
