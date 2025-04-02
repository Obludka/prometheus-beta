def cocktail_shaker_sort(arr):
    """
    Implement the cocktail shaker sort (bidirectional bubble sort) algorithm.
    
    This sorting algorithm is a variation of bubble sort that sorts in both 
    directions. It works by doing a bubble sort pass from left to right, 
    then from right to left, reducing the number of comparisons in each pass.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    """
    # Create a copy of the input list to avoid modifying the original
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a mutable copy of the list
    sorted_arr = arr.copy()
    
    # Flag to track if any swaps occurred
    swapped = True
    start = 0
    end = len(sorted_arr) - 1
    
    while swapped:
        # Reset swapped flag
        swapped = False
        
        # Forward pass (left to right)
        for i in range(start, end):
            try:
                if sorted_arr[i] > sorted_arr[i + 1]:
                    # Swap elements
                    sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                    swapped = True
            except TypeError:
                raise ValueError("List contains elements that cannot be compared")
        
        # If no swapping occurred, list is sorted
        if not swapped:
            break
        
        # Reset swapped flag
        swapped = False
        
        # Reduce end point
        end -= 1
        
        # Backward pass (right to left)
        for i in range(end - 1, start - 1, -1):
            try:
                if sorted_arr[i] > sorted_arr[i + 1]:
                    # Swap elements
                    sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                    swapped = True
            except TypeError:
                raise ValueError("List contains elements that cannot be compared")
        
        # Increase start point
        start += 1
    
    return sorted_arr