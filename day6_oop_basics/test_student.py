import pytest
from student import Student


def test_create_student_default_grades():
    s = Student("Sana", 101)
    assert s.name == "Sana"
    assert s.student_id == 101
    assert s.grades == []


def test_create_student_with_initial_grades():
    s = Student("Mona", "A1", [90, 80, 70])
    assert s.grades == [90, 80, 70]


def test_add_grade():
    s = Student("Sana", 101)
    s.add_grade(95)
    assert s.grades == [95.0]


def test_add_grade_multiple():
    s = Student("Sana", 101)
    s.add_grade(80)
    s.add_grade(100)
    assert s.grades == [80.0, 100.0]


def test_add_grade_type_error():
    s = Student("Sana", 101)
    with pytest.raises(TypeError):
        s.add_grade("A+")  # not a number


def test_get_average_empty_returns_zero():
    s = Student("Sana", 101)
    assert s.get_average() == 0.0


def test_get_average_correct():
    s = Student("Sana", 101)
    s.add_grade(80)
    s.add_grade(100)
    assert s.get_average() == 90.0


def test_str_contains_main_info():
    s = Student("Sana", 101, [100, 80])
    text = str(s)
    assert "Student(" in text
    assert "name=Sana" in text
    assert "id=101" in text
    assert "grades=[100, 80]" in text
    assert "average=90.00" in text
