import pytest
from src.stack_list_reversal import reverse_list_with_stack, Stack

def test_stack_initialization():
    """Test basic stack initialization and operations."""
    stack = Stack()
    assert stack.is_empty() == True
    
    stack.push(1)
    assert stack.is_empty() == False
    
    item = stack.pop()
    assert item == 1
    assert stack.is_empty() == True

def test_reverse_list_normal_case():
    """Test reversing a list with multiple elements."""
    test_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_with_stack(test_list)
    assert reversed_list == [5, 4, 3, 2, 1]
    # Ensure original list is not modified
    assert test_list == [1, 2, 3, 4, 5]

def test_reverse_empty_list():
    """Test reversing an empty list."""
    test_list = []
    reversed_list = reverse_list_with_stack(test_list)
    assert reversed_list == []

def test_reverse_single_element_list():
    """Test reversing a list with a single element."""
    test_list = [42]
    reversed_list = reverse_list_with_stack(test_list)
    assert reversed_list == [42]

def test_reverse_list_with_duplicates():
    """Test reversing a list with duplicate elements."""
    test_list = [1, 2, 2, 3, 1]
    reversed_list = reverse_list_with_stack(test_list)
    assert reversed_list == [1, 3, 2, 2, 1]

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_list_with_stack("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_list_with_stack(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_list_with_stack(None)

def test_stack_pop_empty():
    """Test popping from an empty stack raises an IndexError."""
    stack = Stack()
    with pytest.raises(IndexError, match="Cannot pop from an empty stack"):
        stack.pop()