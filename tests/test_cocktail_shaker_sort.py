import pytest
from src.cocktail_shaker_sort import cocktail_shaker_sort

def test_cocktail_shaker_sort_basic():
    """Test basic sorting of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_already_sorted():
    """Test list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert cocktail_shaker_sort(input_list) == input_list

def test_cocktail_shaker_sort_reverse_sorted():
    """Test list sorted in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_empty_list():
    """Test empty list"""
    assert cocktail_shaker_sort([]) == []

def test_cocktail_shaker_sort_single_element():
    """Test list with a single element"""
    input_list = [42]
    assert cocktail_shaker_sort(input_list) == input_list

def test_cocktail_shaker_sort_duplicate_elements():
    """Test list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_with_strings():
    """Test sorting strings"""
    input_list = ['banana', 'apple', 'cherry', 'date']
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_negative_numbers():
    """Test sorting list with negative numbers"""
    input_list = [-5, 3, -2, 0, 1, -7, 4]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        cocktail_shaker_sort("not a list")

def test_cocktail_shaker_sort_uncomparable_elements():
    """Test that ValueError is raised for uncomparable elements"""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        cocktail_shaker_sort([1, 2, '3'])