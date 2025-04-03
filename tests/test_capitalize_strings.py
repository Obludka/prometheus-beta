import pytest
from src.capitalize_strings import capitalize_strings

def test_basic_capitalization():
    """Test basic string capitalization."""
    input_list = ["hello", "world", "python"]
    expected = ["Hello", "World", "Python"]
    assert capitalize_strings(input_list) == expected

def test_already_capitalized():
    """Test that already capitalized strings remain the same."""
    input_list = ["Hello", "World"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_list) == expected

def test_mixed_case():
    """Test mixed case capitalization."""
    input_list = ["hELLo", "wORLd"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_list) == expected

def test_empty_list():
    """Test capitalization of an empty list."""
    assert capitalize_strings([]) == []

def test_single_element_list():
    """Test capitalization of a single-element list."""
    assert capitalize_strings(["test"]) == ["Test"]

def test_invalid_input_not_list():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        capitalize_strings("not a list")

def test_invalid_input_non_string_elements():
    """Test that list with non-string elements raises TypeError."""
    with pytest.raises(TypeError, match="All elements in the list must be strings"):
        capitalize_strings(["valid", 42, "string"])

def test_whitespace_capitalization():
    """Test capitalization with whitespace strings."""
    input_list = [" hello", "\tworld"]
    expected = [" hello", "\tworld"]
    assert capitalize_strings(input_list) == expected