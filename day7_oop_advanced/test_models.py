import pytest
from models import Student, GraduateStudent, Professor, Course


def test_student_add_grade_and_average():
    s = Student("Sana", 1)
    s.add_grade(80)
    s.add_grade(100)
    assert s.get_average() == 90.0


def test_student_private_grades_access():
    s = Student("Sana", 1)
    s.add_grade(90)
    # grades are private, but we can read via getter
    assert s.get_grades() == [90.0]


def test_student_add_grade_type_error():
    s = Student("Sana", 1)
    with pytest.raises(TypeError):
        s.add_grade("A+")


def test_graduate_student_inheritance_and_thesis():
    gs = GraduateStudent("Mona", "G1", "AI for Healthcare")
    assert gs.name == "Mona"
    assert gs.student_id == "G1"
    assert gs.thesis_title == "AI for Healthcare"


def test_graduate_student_overridden_str():
    gs = GraduateStudent("Mona", "G1", "AI for Healthcare")
    gs.add_grade(100)
    text = str(gs)
    assert "GraduateStudent" in text
    assert "thesis=AI for Healthcare" in text
    assert "avg=100.00" in text


def test_professor_assign_grade():
    p = Professor("Dr. Ahmad", 10)
    s = Student("Sana", 1)
    p.assign_grade(s, 95)
    assert s.get_grades() == [95.0]


def test_course_composition_enroll_drop():
    c = Course("CS101", "Intro to OOP")
    s1 = Student("Sana", 1)
    s2 = GraduateStudent("Mona", "G1", "AI Thesis")

    c.enroll(s1)
    c.enroll(s2)
    assert len(c.students) == 2

    c.drop(s1)
    assert len(c.students) == 1
    assert c.students[0] == s2


def test_course_class_average():
    c = Course("CS101", "Intro to OOP")
    s1 = Student("Sana", 1)
    s2 = Student("Sara", 2)

    s1.add_grade(80)
    s2.add_grade(100)

    c.enroll(s1)
    c.enroll(s2)

    assert c.class_average() == 90.0
