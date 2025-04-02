import pytest
from src.median_index import find_median_index

def test_odd_length_array():
    """Test median index for odd-length sorted array."""
    arr = [1, 2, 3, 4, 5]
    assert find_median_index(arr) == 2  # Middle index

def test_even_length_array():
    """Test median value for even-length sorted array."""
    arr = [1, 2, 3, 4]
    assert find_median_index(arr) == 2.5  # Average of 2 and 3

def test_single_element_array():
    """Test median index for single-element array."""
    arr = [42]
    assert find_median_index(arr) == 0  # Only index is 0

def test_two_element_array():
    """Test median value for two-element array."""
    arr = [1, 3]
    assert find_median_index(arr) == 2.0  # Average of 1 and 3

def test_empty_array_raises_error():
    """Test that empty array raises ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_median_index([])

def test_non_list_input_raises_error():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median_index("not a list")

def test_large_array():
    """Test median index for a larger odd-length sorted array."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert find_median_index(arr) == 4  # Middle index

def test_large_even_array():
    """Test median value for a larger even-length sorted array."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert find_median_index(arr) == 4.5  # Average of 4 and 5