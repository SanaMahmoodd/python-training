class Student:
    def __init__(self, name: str, student_id: int | str, grades=None):
        self.name = name
        self.student_id = student_id
        self.grades = list(grades) if grades is not None else []

    def add_grade(self, grade: float) -> None:
        if not isinstance(grade, (int, float)):
            raise TypeError("grade must be a number")
        self.grades.append(float(grade))

    def get_average(self) -> float:
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self) -> str:
        avg = self.get_average()
        return f"Student(name={self.name}, id={self.student_id}, grades={self.grades}, average={avg:.2f})"
