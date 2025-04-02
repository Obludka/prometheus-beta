import pytest
from src.string_permutations import generate_unique_permutations

def test_generate_unique_permutations_basic():
    """Test basic string permutations."""
    result = generate_unique_permutations('abc')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert sorted(result) == sorted(expected)

def test_generate_unique_permutations_empty_string():
    """Test empty string case."""
    assert generate_unique_permutations('') == []

def test_generate_unique_permutations_single_char():
    """Test single character string."""
    assert generate_unique_permutations('a') == ['a']

def test_generate_unique_permutations_duplicate_chars():
    """Test string with duplicate characters."""
    result = generate_unique_permutations('abb')
    expected = ['abb', 'bab', 'bba']
    assert sorted(result) == sorted(expected)

def test_generate_unique_permutations_invalid_input():
    """Test invalid input type."""
    with pytest.raises(TypeError):
        generate_unique_permutations(123)
    with pytest.raises(TypeError):
        generate_unique_permutations(None)

def test_generate_unique_permutations_large_input():
    """Test functionality with a larger string."""
    result = generate_unique_permutations('abcd')
    assert len(result) == 24  # 4! = 24 unique permutations