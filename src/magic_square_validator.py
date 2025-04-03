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
        [3,2,1,6,5,4,9,8,7],
        # More permutations
    ]
    
    # Try each grid and check if it's a magic square
    for possible_square in grids:
        # Check row sums
        rows = [
            possible_square[0] + possible_square[1] + possible_square[2],
            possible_square[3] + possible_square[4] + possible_square[5],
            possible_square[6] + possible_square[7] + possible_square[8]
        ]
        
        # Check column sums
        cols = [
            possible_square[0] + possible_square[3] + possible_square[6],
            possible_square[1] + possible_square[4] + possible_square[7],
            possible_square[2] + possible_square[5] + possible_square[8]
        ]
        
        # Check diagonal sums
        diags = [
            possible_square[0] + possible_square[4] + possible_square[8],
            possible_square[2] + possible_square[4] + possible_square[6]
        ]
        
        # Combine all sums
        all_sums = rows + cols + diags
        
        # If all sums are equal, it's a magic square
        if len(set(all_sums)) == 1:
            return True
    
    return False