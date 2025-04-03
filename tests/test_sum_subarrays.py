import pytest
from src.sum_subarrays import sum_subarrays

def test_basic_functionality():
    """Test basic functionality with a simple sorted list"""
    arr = [1, 2, 3, 4]
    k = 2
    # Expected subarrays: 
    # Length 1: [1], [2], [3], [4]
    # Length 2: [1,2], [2,3], [3,4]
    # Sum = (1) + (2) + (3) + (4) + (1+2) + (2+3) + (3+4) = 22
    assert sum_subarrays(arr, k) == 22

def test_k_is_zero():
    """Test when k is zero"""
    arr = [1, 2, 3, 4]
    assert sum_subarrays(arr, 0) == 0

def test_empty_array():
    """Test with an empty array"""
    arr = []
    assert sum_subarrays(arr, 5) == 0

def test_k_greater_than_array_length():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    k = 5
    # Sum of all subarrays
    assert sum_subarrays(arr, k) == 24

def test_single_element_array():
    """Test with a single-element array"""
    arr = [42]
    assert sum_subarrays(arr, 1) == 42

def test_type_error_non_list():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input 'arr' must be a list"):
        sum_subarrays("not a list", 2)

def test_type_error_non_integer_k():
    """Test that TypeError is raised for non-integer k"""
    with pytest.raises(TypeError, match="Input 'k' must be an integer"):
        sum_subarrays([1, 2, 3], "2")

def test_value_error_negative_k():
    """Test that ValueError is raised for negative k"""
    with pytest.raises(ValueError, match="Input 'k' must be non-negative"):
        sum_subarrays([1, 2, 3], -1)

def test_value_error_non_numeric_elements():
    """Test that ValueError is raised for non-numeric elements"""
    with pytest.raises(ValueError, match="All elements in 'arr' must be numeric"):
        sum_subarrays([1, 2, "3"], 2)

def test_floating_point_numbers():
    """Test that function works with floating point numbers"""
    arr = [1.5, 2.5, 3.5]
    k = 2
    # Manual calculation of expected sum
    expected_sum = (1.5) + (2.5) + (3.5) + (1.5 + 2.5) + (2.5 + 3.5)
    assert sum_subarrays(arr, k) == pytest.approx(expected_sum)