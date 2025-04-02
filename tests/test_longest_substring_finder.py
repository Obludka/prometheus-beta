import pytest
from src.longest_substring_finder import find_longest_substring

def test_find_longest_substring_basic():
    """Test basic functionality of finding longest substring."""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_find_longest_substring_case_sensitivity():
    """Ensure the function is case-sensitive."""
    assert find_longest_substring("ABCabcABC") == "ABCabc"
    assert find_longest_substring("aAaA") == "aA"

def test_find_longest_substring_edge_cases():
    """Test edge cases like empty string and single character."""
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("aab") == "ab"

def test_find_longest_substring_special_characters():
    """Test with special characters and mixed input."""
    assert find_longest_substring("!@#$%^&*()") == "!@#$%^&*()"
    assert find_longest_substring("abcd123!@#") == "abcd123!@#"

def test_find_longest_substring_repeated_pattern():
    """Test scenarios with repeated patterns."""
    assert find_longest_substring("dvdf") == "vdf"
    assert find_longest_substring("tmmzuxt") == "mzuxt"