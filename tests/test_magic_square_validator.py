import pytest
from src.magic_square_validator import is_magic_square

def test_valid_magic_square():
    # Test a valid magic square configuration
    assert is_magic_square([1,2,3,4,5,6,7,8,9,0]) == True
    assert is_magic_square([1,2,3,4,5,6,7,8,9,1]) == True

def test_invalid_length():
    # Test incorrect list length
    with pytest.raises(ValueError):
        is_magic_square([1,2,3,4,5,6,7,8])  # Too short
    with pytest.raises(ValueError):
        is_magic_square([1,2,3,4,5,6,7,8,9,10,11])  # Too long

def test_non_unique_numbers():
    # Test non-unique numbers
    assert is_magic_square([1,1,3,4,5,6,7,8,9,0]) == False

def test_out_of_range_numbers():
    # Test numbers outside 1-9 range
    assert is_magic_square([1,2,3,4,5,6,7,8,10,0]) == False

def test_invalid_grid_order():
    # Test invalid grid order
    assert is_magic_square([1,2,3,4,5,6,7,8,9,10]) == False

def test_non_magic_square():
    # Test configurations that don't sum correctly
    assert is_magic_square([1,2,3,4,5,6,7,8,9,2]) == False

def test_edge_cases():
    # Additional edge cases
    assert is_magic_square([9,8,7,6,5,4,3,2,1,0]) == False
    assert is_magic_square([1,1,1,1,1,1,1,1,1,0]) == False