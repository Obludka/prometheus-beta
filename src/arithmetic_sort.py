def arithmetic_sort(arr):
    """
    Sort a list of integers using only basic arithmetic operations.
    
    This function implements a custom sorting algorithm that does not use 
    built-in sorting functions, relying only on basic arithmetic operations.
    
    Args:
        arr (list): A list of integers to be sorted.
    
    Returns:
        list: A new list with integers sorted in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Convert to list of numbers to ensure all elements are integers
    try:
        nums = [int(x) for x in arr]
    except (ValueError, TypeError):
        raise TypeError("All elements must be integers")
    
    # Bubble sort using only arithmetic operations
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare and swap using only arithmetic
            if nums[j] > nums[j + 1]:
                # Swap without using temp variable
                nums[j] = nums[j] + nums[j + 1]
                nums[j + 1] = nums[j] - nums[j + 1]
                nums[j] = nums[j] - nums[j + 1]
    
    return nums