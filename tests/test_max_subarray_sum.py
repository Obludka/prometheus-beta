import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_functionality():
    """Test basic functionality with a simple array."""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_element_array():
    """Test an array with a single element."""
    arr = [5]
    assert max_subarray_sum(arr, 1) == 5

def test_negative_numbers():
    """Test an array with negative numbers."""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == -6  # -1 + -2 + -3

def test_mixed_numbers():
    """Test an array with mixed positive and negative numbers."""
    arr = [2, -1, 3, 10, -4, 7, 2, -5]
    k = 3
    assert max_subarray_sum(arr, k) == 13  # Actual max sum is 13 (3 + 10 + -4)

def test_full_array_sum():
    """Test when k equals the length of the array."""
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr, 5) == 15

def test_invalid_k_too_large():
    """Test when k is larger than the array length."""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length \\(k\\) cannot be larger than the input array"):
        max_subarray_sum(arr, 4)

def test_invalid_k_negative():
    """Test when k is negative."""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length \\(k\\) must be a positive integer"):
        max_subarray_sum(arr, -1)

def test_none_input():
    """Test when input array is None."""
    with pytest.raises(ValueError, match="Input array cannot be None"):
        max_subarray_sum(None, 3)

def test_empty_input():
    """Test when input array is empty."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        max_subarray_sum([], 3)