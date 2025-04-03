def filter_unique_multiples(numbers):
    """
    Filter a list of integers to return only those that are multiples of 3 or 5, but not both.
    
    Args:
        numbers (list): A list of integers to filter
    
    Returns:
        list: A sorted list of integers that are multiples of 3 or 5, but not both
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate list contains only integers
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers")
    
    # Filter numbers that are multiples of 3 or 5, but not both
    unique_multiples = [
        num for num in numbers 
        if (num % 3 == 0) != (num % 5 == 0)
    ]
    
    # Return sorted list
    return sorted(unique_multiples)