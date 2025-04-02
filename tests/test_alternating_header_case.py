import pytest
from src.alternating_header_case import convert_to_alternating_header_case

def test_basic_conversion():
    """Test basic string conversion to alternating header case."""
    assert convert_to_alternating_header_case("hello world python") == "Hello world Python"

def test_mixed_case_input():
    """Test conversion when input has mixed case."""
    assert convert_to_alternating_header_case("PYTHON is AWESOME") == "Python is Awesome"

def test_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_header_case("") == ""

def test_single_word():
    """Test conversion of a single word."""
    assert convert_to_alternating_header_case("hello") == "Hello"

def test_multiple_words():
    """Test conversion of multiple words."""
    assert convert_to_alternating_header_case("this is a test string") == "This is A test String"

def test_input_type_error():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_header_case(123)

def test_whitespace_handling():
    """Test handling of extra whitespace."""
    assert convert_to_alternating_header_case("  hello   world  ") == "Hello world"

def test_single_character_words():
    """Test handling of single character words."""
    assert convert_to_alternating_header_case("a b c d") == "A b C d"