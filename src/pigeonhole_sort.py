def pigeonhole_sort(arr):
    """
    Implement the Pigeonhole Sort algorithm.
    
    Pigeonhole sort is an efficient sorting algorithm for sorting arrays 
    with a limited range of values. It works by distributing elements into 
    a set of "pigeonholes" and then collecting them back in order.
    
    Args:
        arr (list): The input list of integers to be sorted.
    
    Returns:
        list: A new sorted list containing the same elements as the input.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    
    Time Complexity: O(n + range), where n is the number of elements
    Space Complexity: O(range), where range is the difference between 
                      the maximum and minimum elements
    
    Example:
        >>> pigeonhole_sort([8, 3, 2, 7, 4, 6, 8])
        [2, 3, 4, 6, 7, 8, 8]
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Find the range of the input
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1
    
    # Create pigeonholes
    pigeonholes = [0] * range_val
    
    # Count occurrences of each element
    for num in arr:
        pigeonholes[num - min_val] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(range_val):
        # Add each number its correct number of times
        while pigeonholes[i] > 0:
            sorted_arr.append(i + min_val)
            pigeonholes[i] -= 1
    
    return sorted_arr