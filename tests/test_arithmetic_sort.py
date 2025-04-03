import pytest
from src.arithmetic_sort import arithmetic_sort

def test_arithmetic_sort_basic():
    """Test sorting a simple list of integers."""
    input_list = [5, 2, 9, 1, 7]
    expected = [1, 2, 5, 7, 9]
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_empty_list():
    """Test sorting an empty list."""
    assert arithmetic_sort([]) == []

def test_arithmetic_sort_single_element():
    """Test sorting a list with a single element."""
    assert arithmetic_sort([42]) == [42]

def test_arithmetic_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == input_list

def test_arithmetic_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_type_error_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        arithmetic_sort("not a list")

def test_arithmetic_sort_type_error_non_integers():
    """Test that a TypeError is raised for lists with non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        arithmetic_sort([1, 2, "three", 4])

def test_arithmetic_sort_large_numbers():
    """Test sorting with large numbers."""
    input_list = [1000000, -500000, 750000, -250000, 500000]
    expected = [-500000, -250000, 500000, 750000, 1000000]
    assert arithmetic_sort(input_list) == expected