import pytest
from contacts.utils import strong_password, WeakPasswordError

def test_valid_password():
    assert strong_password("Abc123!@") is True

def test_short_password():
    with pytest.raises(WeakPasswordError):
        strong_password("Ab1!")

def test_missing_uppercase():
    with pytest.raises(WeakPasswordError):
        strong_password("abc123!@")

def test_missing_number():
    with pytest.raises(WeakPasswordError):
        strong_password("Abcdef!@")

def test_missing_special():
    with pytest.raises(WeakPasswordError):
        strong_password("Abc12345")
