import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome cases"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True

def test_non_palindromes():
    """Test non-palindrome cases"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_case_insensitive():
    """Test that palindrome checks are case-insensitive"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_ignore_punctuation():
    """Test that non-alphanumeric characters are ignored"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car!") == False

def test_edge_cases():
    """Test edge cases"""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Whitespace
    assert is_palindrome("a") == True  # Single character

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])