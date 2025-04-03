def sum_subarrays(arr, k):
    """
    Calculate the sum of all elements in subarrays with length less than or equal to k.
    
    Args:
        arr (list): A sorted list of integers
        k (int): Maximum length of subarrays to consider
    
    Returns:
        int: Sum of all elements in valid subarrays
    
    Raises:
        TypeError: If arr is not a list or k is not an integer
        ValueError: If k is negative or arr contains non-numeric elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input 'arr' must be a list")
    if not isinstance(k, int):
        raise TypeError("Input 'k' must be an integer")
    if k < 0:
        raise ValueError("Input 'k' must be non-negative")
    
    # Check for non-numeric elements
    if any(not isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements in 'arr' must be numeric")
    
    # If k is 0 or arr is empty, return 0
    if k == 0 or not arr:
        return 0
    
    total_sum = 0
    n = len(arr)
    
    # Cumulative sum tracking
    for start in range(n):
        current_sum = 0
        for length in range(1, min(k + 1, n - start + 1)):
            current_sum += arr[start + length - 1]
            total_sum += current_sum
    
    return total_sum