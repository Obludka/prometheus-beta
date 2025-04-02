def find_closest_pair_sum(arr, target):
    """
    Find the pair of elements in an array whose sum is closest to the target value.
    
    Args:
        arr (list): A list of integers to search for pairs
        target (int): The target sum to find the closest pair to
    
    Returns:
        tuple: A tuple containing the two elements that form the pair with sum closest to target,
               or None if the input array has fewer than 2 elements
    
    Raises:
        TypeError: If input is not a list or target is not a number
        ValueError: If the list contains non-numeric elements
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be a number")
    
    # Check if array has at least 2 elements
    if len(arr) < 2:
        return None
    
    # Validate array contains only numbers
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Array must contain only numeric elements")
    
    # Initialize variables to track closest pair
    closest_diff = float('inf')
    closest_pair = None
    first_occurrence = True
    
    # Nested loops to check all possible pairs
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]
            current_diff = abs(current_sum - target)
            
            # Update if this pair is closer to target 
            # Or the first occurrence of equally close pairs
            if (current_diff < closest_diff or 
                (current_diff == closest_diff and first_occurrence)):
                closest_diff = current_diff
                closest_pair = (arr[i], arr[j])
                first_occurrence = False
    
    return closest_pair