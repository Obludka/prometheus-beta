def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a contiguous subarray with length k.

    Args:
        arr (list): A list of integers to search through.
        k (int): The length of the contiguous subarray.

    Returns:
        int: The maximum sum of a contiguous subarray of length k.

    Raises:
        ValueError: If the input array is None, empty, or k is invalid.
    """
    # Validate input
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    if k <= 0:
        raise ValueError("Subarray length (k) must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length (k) cannot be larger than the input array")
    
    # If k equals array length, return the sum of the entire array
    if k == len(arr):
        return sum(arr)
    
    # Use sliding window technique
    # Start with the sum of first k elements
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window and update max_sum
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add the next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum