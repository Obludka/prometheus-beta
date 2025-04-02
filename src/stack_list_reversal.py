class Stack:
    """
    A simple stack implementation using a list.
    Provides basic stack operations: push, pop, and is_empty.
    """
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack.
        """
        self._items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self._items.pop()
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0


def reverse_list_with_stack(input_list):
    """
    Reverse a list of integers using a stack-based approach.
    
    This function uses a stack to efficiently reverse the order of elements 
    in the input list. It has O(n) time complexity and O(n) space complexity.
    
    Args:
        input_list (list): A list of integers to be reversed.
    
    Returns:
        list: A new list with elements in reversed order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input type
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list or single-element list efficiently
    if len(input_list) <= 1:
        return input_list.copy()
    
    # Create a stack
    stack = Stack()
    
    # Push all elements to the stack
    for item in input_list:
        stack.push(item)
    
    # Create a new list by popping from the stack
    reversed_list = []
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    
    return reversed_list