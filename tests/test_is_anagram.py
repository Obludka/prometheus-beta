import pytest
from src.is_anagram import is_anagram

def test_basic_anagrams():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True

def test_case_insensitive():
    assert is_anagram("Debit Card", "Bad Credit") == True
    assert is_anagram("Tea", "Eat") == True

def test_non_anagrams():
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "javascript") == False

def test_whitespace_handling():
    assert is_anagram("rail safety", "fairy tales") == True
    assert is_anagram("  stop  ", "  post  ") == True

def test_empty_strings():
    assert is_anagram("", "") == True

def test_single_character():
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False

def test_unicode_characters():
    assert is_anagram("über", "rebü") == True

def test_invalid_input_types():
    with pytest.raises(TypeError):
        is_anagram(123, "hello")
    with pytest.raises(TypeError):
        is_anagram("hello", None)
    with pytest.raises(TypeError):
        is_anagram([], "hello")

def test_different_lengths():
    assert is_anagram("abc", "abcd") == False
    assert is_anagram("a", "") == False