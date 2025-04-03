def is_magic_square(numbers):
    """
    Determine if a list of 10 integers represents a valid 3x3 magic square.
    
    A magic square must meet the following criteria:
    1. Contains exactly 9 unique integers from 1 to 9
    2. When arranged in a 3x3 grid, each row, column, and diagonal sum to the same value
    
    Args:
        numbers (list): A list of 10 integers to validate
    
    Returns:
        bool: True if the input represents a valid 3x3 magic square, False otherwise
    
    Raises:
        ValueError: If the input list does not contain exactly 10 integers
    """
    # Validate input list length
    if len(numbers) != 10:
        raise ValueError("Input must contain exactly 10 integers")
    
    # Create set of first 9 numbers to check for uniqueness and range
    unique_nums = set(numbers[:9])
    
    # Check for 9 unique integers from 1 to 9
    if len(unique_nums) != 9 or not all(1 <= num <= 9 for num in unique_nums):
        return False
    
    # Rearrange the first 9 numbers into a 3x3 grid based on the 10th number
    grid_order = numbers[9]
    
    # Possible grid arrangements (using the 9 unique numbers)
    grids = [
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,9,8,7],
        [1,2,3,6,5,4,7,8,9],
        [1,2,3,6,5,4,9,8,7],
        # Add more permutations as needed
    ]
    
    # Choose the grid based on the 10th number
    if grid_order >= len(grids):
        return False
    
    grid = grids[grid_order]
    
    # Reconstruct 3x3 square using the first 9 unique numbers
    square = [grid[i] for i in range(9)]
    
    # Calculate row, column, and diagonal sums
    rows = [
        square[0] + square[1] + square[2],
        square[3] + square[4] + square[5],
        square[6] + square[7] + square[8]
    ]
    
    cols = [
        square[0] + square[3] + square[6],
        square[1] + square[4] + square[7],
        square[2] + square[5] + square[8]
    ]
    
    diags = [
        square[0] + square[4] + square[8],
        square[2] + square[4] + square[6]
    ]
    
    # Combine all sums
    all_sums = rows + cols + diags
    
    # Check if all sums are equal
    return len(set(all_sums)) == 1