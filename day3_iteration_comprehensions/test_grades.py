import pytest
from grades import top_three_students, pass_fail


def test_top_three_students_basic():
    students = {
        "Ali": 85,
        "Sara": 92,
        "Lina": 47,
        "Omar": 76
    }

    result = top_three_students(students)

    assert result[0][0] == "Sara"
    assert len(result) == 3


def test_pass_fail_results():
    students = {
        "Ali": 40,
        "Sara": 60
    }

    result = pass_fail(students)

    assert result["Ali"] == "fail"
    assert result["Sara"] == "pass"


def test_invalid_grade_value():
    students = {
        "Ali": 120
    }

    with pytest.raises(ValueError):
        pass_fail(students)


def test_invalid_students_type():
    students = ["Ali", "Sara"]

    with pytest.raises(TypeError):
        top_three_students(students)