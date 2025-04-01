def quick_sort(arr):
    """
    Implement the Quick Sort algorithm to sort a list in-place.
    
    Quick Sort is an efficient, divide-and-conquer sorting algorithm 
    with an average time complexity of O(n log n).
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    def _quick_sort_helper(low, high):
        """
        Recursive helper function to perform quick sort.
        
        Args:
            low (int): Starting index of the sublist.
            high (int): Ending index of the sublist.
        """
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = _partition(low, high)
            
            # Recursively sort the left and right subarrays
            _quick_sort_helper(low, pivot_index - 1)
            _quick_sort_helper(pivot_index + 1, high)
    
    def _partition(low, high):
        """
        Partition the sublist using the last element as pivot.
        
        Args:
            low (int): Starting index of the sublist.
            high (int): Ending index of the sublist.
        
        Returns:
            int: The index of the pivot after partitioning.
        """
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Index of smaller element
        i = low - 1
        
        # Traverse through the array
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                # Increment index of smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Call the recursive helper function
    _quick_sort_helper(0, len(arr) - 1)
    
    return arr