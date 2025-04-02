import pytest
from src.pigeonhole_sort import pigeonhole_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    assert pigeonhole_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(arr) == arr

def test_reverse_sorted():
    """Test sorting a reverse sorted list"""
    assert pigeonhole_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicate_elements():
    """Test sorting with duplicate elements"""
    assert pigeonhole_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

def test_empty_list():
    """Test sorting an empty list"""
    assert pigeonhole_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert pigeonhole_sort([42]) == [42]

def test_negative_numbers():
    """Test sorting with negative numbers"""
    assert pigeonhole_sort([-3, -1, -4, 0, 2, -2]) == [-4, -3, -2, -1, 0, 2]

def test_mixed_positive_negative():
    """Test sorting with mixed positive and negative numbers"""
    assert pigeonhole_sort([-5, 2, 0, -3, 4, 1]) == [-5, -3, 0, 1, 2, 4]

def test_type_error_non_list():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        pigeonhole_sort("not a list")

def test_value_error_non_integer():
    """Test that a ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        pigeonhole_sort([1, 2, 'three', 4])

def test_large_range():
    """Test sorting with a large range of numbers"""
    arr = [1000, 10, 5, 1000000, -1000, 0, 42]
    assert pigeonhole_sort(arr) == [-1000, 0, 5, 10, 42, 1000, 1000000]