import pytest
from src.sort_even_squares import sort_array_even_squares

def test_sort_array_even_squares_basic():
    """Test basic functionality of the function."""
    assert sort_array_even_squares([3, 1, 2, 4, 5]) == [1, 3, 5, 16, 4]

def test_sort_array_even_squares_all_odds():
    """Test case with only odd numbers."""
    assert sort_array_even_squares([7, 3, 1, 5]) == [1, 3, 5, 7]

def test_sort_array_even_squares_all_evens():
    """Test case with only even numbers."""
    assert sort_array_even_squares([2, 4, 6, 8]) == [4, 16, 36, 64]

def test_sort_array_even_squares_empty():
    """Test case with an empty list."""
    assert sort_array_even_squares([]) == []

def test_sort_array_even_squares_negative_numbers():
    """Test case with negative numbers."""
    assert sort_array_even_squares([-3, -2, 1, 4, -1]) == [-3, -1, 1, 16, 4]

def test_sort_array_even_squares_invalid_input():
    """Test that an invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        sort_array_even_squares("not a list")