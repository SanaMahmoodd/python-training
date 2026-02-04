import pytest
from bmi import bmi_calculator


def test_valid_bmi_float():
    assert bmi_calculator(1.8, 75) == 23.15


def test_valid_bmi_int():
    assert bmi_calculator(2, 80) == 20.0


def test_invalid_height_value():
    with pytest.raises(ValueError):
        bmi_calculator(0, 70)


def test_invalid_weight_value():
    with pytest.raises(ValueError):
        bmi_calculator(1.7, -5)


def test_invalid_type_height():
    with pytest.raises(TypeError):
        bmi_calculator("1.7", 70)


def test_invalid_type_weight():
    with pytest.raises(TypeError):
        bmi_calculator(1.7, None)


def test_bool_inputs():
    with pytest.raises(TypeError):
        bmi_calculator(True, 70)

    with pytest.raises(TypeError):
        bmi_calculator(1.7, False)
