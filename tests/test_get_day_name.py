import pytest
from datetime import datetime
from src.get_day_name import get_day_name

def test_get_day_name_datetime():
    """Test getting day name from a datetime object"""
    # Known date: 2023-06-21 is a Wednesday
    test_date = datetime(2023, 6, 21)
    assert get_day_name(test_date) == 'Wednesday'

def test_get_day_name_string():
    """Test getting day name from a valid date string"""
    # Known date: 2023-06-21 is a Wednesday
    assert get_day_name('2023-06-21') == 'Wednesday'

def test_get_day_name_different_dates():
    """Test multiple different dates"""
    test_cases = [
        (datetime(2023, 1, 1), 'Sunday'),    # New Year's Day 2023
        (datetime(2023, 12, 25), 'Monday'),  # Christmas 2023
        (datetime(2024, 2, 29), 'Thursday'), # Leap day 2024
    ]
    
    for date, expected_day in test_cases:
        assert get_day_name(date) == expected_day

def test_invalid_date_string():
    """Test handling of invalid date string"""
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_name('invalid-date')

def test_invalid_date_type():
    """Test handling of invalid input type"""
    with pytest.raises(ValueError, match="Input must be a datetime object"):
        get_day_name(123)
        
def test_edge_cases():
    """Test various edge cases"""
    # Minimum and maximum possible dates
    min_date = datetime(1, 1, 1)
    max_date = datetime(9999, 12, 31)
    
    assert isinstance(get_day_name(min_date), str)
    assert isinstance(get_day_name(max_date), str)