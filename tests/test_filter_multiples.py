import pytest
from src.filter_multiples import filter_unique_multiples

def test_basic_filtering():
    """Test basic filtering of multiples"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
    expected = [3, 5, 6, 9, 10]
    assert filter_unique_multiples(input_list) == expected

def test_empty_list():
    """Test with an empty list"""
    assert filter_unique_multiples([]) == []

def test_no_multiples():
    """Test list with no valid multiples"""
    input_list = [1, 2, 4, 7, 11]
    assert filter_unique_multiples(input_list) == []

def test_only_15_excluded():
    """Test that numbers divisible by both 3 and 5 are excluded"""
    input_list = [3, 5, 6, 9, 10, 15]
    expected = [3, 5, 6, 9, 10]
    assert filter_unique_multiples(input_list) == expected

def test_negative_numbers():
    """Test filtering with negative numbers"""
    input_list = [-3, -5, -6, -9, -10, -15]
    expected = [-3, -5, -6, -9, -10]
    assert filter_unique_multiples(input_list) == expected

def test_mixed_numbers():
    """Test filtering with mixed positive and negative numbers"""
    input_list = [-3, 0, 3, 5, -5, 6, -10, 9, 10, 15]
    expected = [-3, 0, 3, 5, -5, 6, -10, 9, 10]
    assert filter_unique_multiples(input_list) == expected

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_unique_multiples("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_unique_multiples(123)

def test_invalid_list_elements():
    """Test that ValueError is raised for non-integer list elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        filter_unique_multiples([1, 2, '3', 4])
    with pytest.raises(ValueError, match="All elements must be integers"):
        filter_unique_multiples([1, 2, 3.5, 4])