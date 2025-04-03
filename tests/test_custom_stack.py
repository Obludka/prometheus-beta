import pytest
from src.custom_stack import CustomStack

def test_stack_initialization():
    """Test stack initialization with default and custom capacity."""
    stack = CustomStack()
    assert stack.get_capacity() == 10
    assert len(stack) == 0
    assert stack.is_empty() is True

    custom_stack = CustomStack(capacity=5)
    assert custom_stack.get_capacity() == 5

def test_push_and_pop():
    """Test pushing and popping items of different types."""
    stack = CustomStack()
    
    # Push various data types
    stack.push(42)
    stack.push("hello")
    stack.push([1, 2, 3])
    stack.push({"key": "value"})
    
    # Check length and pop order
    assert len(stack) == 4
    assert stack.pop() == {"key": "value"}
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 42
    assert stack.is_empty() is True

def test_peek():
    """Test peek operation."""
    stack = CustomStack()
    stack.push(10)
    assert stack.peek() == 10
    assert len(stack) == 1  # peek should not remove the item

def test_stack_overflow():
    """Test stack overflow condition."""
    stack = CustomStack(capacity=3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    with pytest.raises(OverflowError, match="Stack is full"):
        stack.push(4)

def test_stack_underflow():
    """Test stack underflow conditions."""
    stack = CustomStack()
    
    with pytest.raises(IndexError, match="Cannot pop from an empty stack"):
        stack.pop()
    
    with pytest.raises(IndexError, match="Cannot peek an empty stack"):
        stack.peek()

def test_invalid_capacity():
    """Test invalid stack capacity initialization."""
    with pytest.raises(ValueError, match="Stack capacity must be a positive integer"):
        CustomStack(capacity=0)
    
    with pytest.raises(ValueError, match="Stack capacity must be a positive integer"):
        CustomStack(capacity=-5)