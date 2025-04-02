import pytest
from src.vowel_rotation import rotate_vowels

def test_basic_lowercase_rotation():
    """Test basic lowercase vowel rotation"""
    assert rotate_vowels("hello") == "hollo"
    assert rotate_vowels("python") == "pythun"
    assert rotate_vowels("aeiou") == "eioua"

def test_uppercase_rotation():
    """Test uppercase vowel rotation"""
    assert rotate_vowels("HELLO") == "HOLLO"
    assert rotate_vowels("PYTHON") == "PYTHUN"
    assert rotate_vowels("AEIOU") == "EIOUA"

def test_mixed_case_rotation():
    """Test mixed case vowel rotation"""
    assert rotate_vowels("HeLLo") == "HoLLu"
    assert rotate_vowels("pYthOn") == "pYthUn"

def test_no_vowels():
    """Test strings without vowels"""
    assert rotate_vowels("xyz") == "xyz"
    assert rotate_vowels("123") == "123"
    assert rotate_vowels("") == ""

def test_only_vowels():
    """Test strings with only vowels"""
    assert rotate_vowels("a") == "e"
    assert rotate_vowels("U") == "A"
    assert rotate_vowels("aEiOu") == "eIoUa"

def test_complex_string():
    """Test complex strings with mixed characters"""
    assert rotate_vowels("Hello, World!") == "Hollo, Wurld!"
    assert rotate_vowels("Python 3.9") == "Pythun 3.9"