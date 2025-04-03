def sort_array_even_squares(arr):
    """
    Sorts an array of numbers with special handling for even number squares.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Sorted array with even number squares sorted in descending order
    
    Raises:
        TypeError: If input is not a list
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    sorted_arr = sorted(arr)
    
    # Separate even and odd numbers
    even_squares = [num ** 2 for num in sorted_arr if num % 2 == 0]
    odd_numbers = [num for num in sorted_arr if num % 2 != 0]
    
    # Sort even squares in descending order
    even_squares.sort(reverse=True)
    
    # Combine odd numbers and even squares
    result = odd_numbers + even_squares
    
    return result