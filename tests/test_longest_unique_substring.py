import pytest
from src.longest_unique_substring import longest_unique_substring

def test_longest_unique_substring():
    # Test basic cases
    assert longest_unique_substring("abcabcbb") == 3  # "abc"
    assert longest_unique_substring("bbbbb") == 1     # "b"
    assert longest_unique_substring("pwwkew") == 3    # "wke"
    
    # Edge cases
    assert longest_unique_substring("") == 0          # Empty string
    assert longest_unique_substring("a") == 1         # Single character
    
    # More complex cases
    assert longest_unique_substring("dvdf") == 3      # "vdf"
    assert longest_unique_substring("tmmzuxt") == 5   # "mzuxt"
    
    # No repeated characters
    assert longest_unique_substring("abcdefg") == 7   # Entire string is unique
    
    # Repeated characters at different positions
    assert longest_unique_substring("abba") == 2      # "ab" or "ba"
    
    # Mixed case and special characters
    assert longest_unique_substring("A1B2C3d4") == 8  # Entire string
    
    # Unicode characters
    assert longest_unique_substring("αβγδεαβ") == 5   # "αβγδε"