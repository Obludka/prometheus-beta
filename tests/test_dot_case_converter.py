import pytest
from src.dot_case_converter import convert_to_dot_case

def test_convert_to_dot_case_different_input_formats():
    """Test conversion of various input string formats"""
    assert convert_to_dot_case("HelloWorld") == "hello.world"
    assert convert_to_dot_case("hello_world") == "hello.world"
    assert convert_to_dot_case("Hello World") == "hello.world"
    assert convert_to_dot_case("hello-world") == "hello.world"

def test_convert_to_dot_case_edge_cases():
    """Test edge cases of dot case conversion"""
    assert convert_to_dot_case("") == ""
    assert convert_to_dot_case("A") == "a"
    assert convert_to_dot_case("ABC") == "abc"

def test_convert_to_dot_case_multiple_words():
    """Test conversion of strings with multiple words"""
    assert convert_to_dot_case("hello world python") == "hello.world.python"
    assert convert_to_dot_case("HelloWorldPython") == "hello.world.python"
    assert convert_to_dot_case("hello_world_python") == "hello.world.python"

def test_convert_to_dot_case_mixed_separators():
    """Test conversion with mixed separators"""
    assert convert_to_dot_case("Hello_World-Test") == "hello.world.test"

def test_convert_to_dot_case_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        convert_to_dot_case(123)
    with pytest.raises(TypeError):
        convert_to_dot_case(None)

def test_convert_to_dot_case_whitespace():
    """Test handling of extra whitespace"""
    assert convert_to_dot_case("  Hello   World  ") == "hello.world"