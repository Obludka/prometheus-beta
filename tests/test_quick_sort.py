import pytest
from src.quick_sort import quick_sort

def test_quick_sort_normal_case():
    """Test quick sort with a normal list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert quick_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_quick_sort_already_sorted():
    """Test quick sort with a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]

def test_quick_sort_reverse_sorted():
    """Test quick sort with a list sorted in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]

def test_quick_sort_with_duplicates():
    """Test quick sort with a list containing duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert quick_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_quick_sort_empty_list():
    """Test quick sort with an empty list."""
    arr = []
    assert quick_sort(arr) == []

def test_quick_sort_single_element():
    """Test quick sort with a single-element list."""
    arr = [42]
    assert quick_sort(arr) == [42]

def test_quick_sort_with_negative_numbers():
    """Test quick sort with negative numbers."""
    arr = [-4, 2, -7, 1, 0, -3]
    assert quick_sort(arr) == [-7, -4, -3, 0, 1, 2]

def test_quick_sort_with_floating_point():
    """Test quick sort with floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert quick_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_quick_sort_type_error():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort(None)