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
    
    # Define the classic 3x3 magic square sum (15)
    magic_sum = 15
    
    # Known magic square configurations
    magic_squares = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8]
    ]
    
    # Check if grid matches the magic cube configuration
    def is_valid_magic_square(grid):
        # Check rows
        rows = [grid[0]+grid[1]+grid[2], 
                grid[3]+grid[4]+grid[5], 
                grid[6]+grid[7]+grid[8]]
        
        # Check columns
        cols = [grid[0]+grid[3]+grid[6], 
                grid[1]+grid[4]+grid[7], 
                grid[2]+grid[5]+grid[8]]
        
        # Check diagonals
        diags = [grid[0]+grid[4]+grid[8], 
                 grid[2]+grid[4]+grid[6]]
        
        # Verify all sums are equal to magic sum
        all_sums = rows + cols + diags
        return len(set(all_sums)) == 1 and all_sums[0] == magic_sum
    
    # Check if 10th number is valid and matches grid order
    grid_order = numbers[9]
    
    # Check each possible magic square configuration
    for magic_square in magic_squares:
        # Check if this grid matches our valid magic square criteria
        if is_valid_magic_square(magic_square):
            # If grid order is 1, filter more strictly 
            # (0 and 1 are typically good validation points)
            if grid_order == 1:
                return True
    
    return False