class Student:
    def __init__(self, name: str, student_id: int | str):
        self.name = name
        self.student_id = student_id
        self.__grades: list[float] = []  # private

    def add_grade(self, grade: float) -> None:
        if not isinstance(grade, (int, float)):
            raise TypeError("grade must be a number")
        self.__grades.append(float(grade))

    def get_average(self) -> float:
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

    def get_grades(self) -> list[float]:
        # controlled access to private grades
        return list(self.__grades)

    def __str__(self) -> str:
        return f"Student(name={self.name}, id={self.student_id}, avg={self.get_average():.2f})"


class GraduateStudent(Student):
    def __init__(self, name: str, student_id: int | str, thesis_title: str):
        super().__init__(name, student_id)  # super()
        self.thesis_title = thesis_title

    def __str__(self) -> str:  # overriding
        return f"GraduateStudent(name={self.name}, id={self.student_id}, thesis={self.thesis_title}, avg={self.get_average():.2f})"


class Professor:
    def __init__(self, name: str, professor_id: int | str):
        self.name = name
        self.professor_id = professor_id

    def assign_grade(self, student: Student, grade: float) -> None:
        # professor assigns grade to any Student (or subclass)
        student.add_grade(grade)

    def __str__(self) -> str:
        return f"Professor(name={self.name}, id={self.professor_id})"


class Course:
    """
    Composition: Course HAS students (contains them), it does NOT inherit from them.
    """
    def __init__(self, code: str, title: str):
        self.code = code
        self.title = title
        self.students: list[Student] = []

    def enroll(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)

    def drop(self, student: Student) -> None:
        if student in self.students:
            self.students.remove(student)

    def class_average(self) -> float:
        if not self.students:
            return 0.0
        return sum(s.get_average() for s in self.students) / len(self.students)

    def __str__(self) -> str:
        return f"Course(code={self.code}, title={self.title}, students={len(self.students)})"
