def find_median_index(arr):
    """
    Find the median index or median value in a sorted array of integers.

    Args:
        arr (list): A sorted list of integers.

    Returns:
        float or int: For odd-length arrays, returns the index of the median element.
                      For even-length arrays, returns the average of the two middle elements.

    Raises:
        ValueError: If the input array is empty.
        TypeError: If the input is not a list.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # Calculate median index
    mid = len(arr) // 2
    
    # If array length is odd, return the middle index
    if len(arr) % 2 == 1:
        return mid
    
    # If array length is even, return average of two middle elements
    return (arr[mid-1] + arr[mid]) / 2