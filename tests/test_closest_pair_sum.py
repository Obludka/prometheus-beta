import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_basic_closest_pair():
    """Test finding the closest pair in a simple scenario"""
    arr = [1, 2, 3, 4, 5]
    target = 7
    assert find_closest_pair_sum(arr, target) == (2, 5)

def test_exact_match():
    """Test a scenario where an exact match exists"""
    arr = [1, 3, 4, 7, 10]
    target = 7
    assert find_closest_pair_sum(arr, target) == (3, 4)

def test_multiple_equal_close_pairs():
    """Ensure the first occurrence of equally close pairs is returned"""
    arr = [1, 5, 4, 3, 7]
    target = 8
    assert find_closest_pair_sum(arr, target) == (1, 7)

def test_negative_numbers():
    """Test functionality with negative numbers"""
    arr = [-1, -5, 4, 3, 7]
    target = 2
    assert find_closest_pair_sum(arr, target) == (-1, 3)

def test_less_than_two_elements():
    """Test handling of lists with fewer than 2 elements"""
    arr = [1]
    assert find_closest_pair_sum(arr, 5) is None
    assert find_closest_pair_sum([], 5) is None

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_closest_pair_sum("not a list", 5)
    
    with pytest.raises(TypeError, match="Target must be a number"):
        find_closest_pair_sum([1, 2, 3], "not a number")

def test_non_numeric_elements():
    """Test error handling for non-numeric list elements"""
    with pytest.raises(ValueError, match="Array must contain only numeric elements"):
        find_closest_pair_sum([1, 2, "three"], 5)

def test_floating_point_target():
    """Test functionality with floating point target"""
    arr = [1.5, 2.5, 3.5, 4.5, 5.5]
    target = 7.0
    assert find_closest_pair_sum(arr, target) == (1.5, 5.5)

def test_large_array():
    """Test with a larger array"""
    arr = list(range(1, 101))  # 1 to 100
    target = 150
    result = find_closest_pair_sum(arr, target)
    assert result == (50, 100)  # Mathematically closest pair