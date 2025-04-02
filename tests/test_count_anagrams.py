import pytest
from src.count_anagrams import count_anagrams

def test_count_anagrams_basic():
    """Test basic functionality of count_anagrams"""
    assert count_anagrams('abab') == 6
    assert count_anagrams('aa') == 2

def test_count_anagrams_single_char():
    """Test single character string"""
    assert count_anagrams('a') == 1

def test_count_anagrams_repeated_chars():
    """Test string with repeated characters"""
    assert count_anagrams('aaaa') == 1

def test_count_anagrams_unique_chars():
    """Test string with unique characters"""
    assert count_anagrams('abcde') == 15  # All unique characters

def test_count_anagrams_invalid_input():
    """Test invalid input handling"""
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        count_anagrams('')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        count_anagrams('AbCd')  # Contains uppercase letters
    
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        count_anagrams('ab cd')  # Contains spaces
    
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        count_anagrams('ab123')  # Contains numbers