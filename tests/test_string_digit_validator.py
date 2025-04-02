import pytest
from src.string_digit_validator import is_digits_only

def test_is_digits_only_valid_input():
    """Test valid digit-only inputs."""
    assert is_digits_only("12345") == True
    assert is_digits_only("0") == True
    assert is_digits_only("9876543210") == True

def test_is_digits_only_invalid_input():
    """Test inputs with non-digit characters."""
    assert is_digits_only("123a45") == False
    assert is_digits_only("12 345") == False
    assert is_digits_only("") == False
    assert is_digits_only("-123") == False
    assert is_digits_only(".123") == False

def test_is_digits_only_type_error():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        is_digits_only(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        is_digits_only(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        is_digits_only(["123"])

def test_is_digits_only_whitespace():
    """Test inputs with whitespace."""
    assert is_digits_only(" ") == False
    assert is_digits_only("\t") == False
    assert is_digits_only("\n") == False