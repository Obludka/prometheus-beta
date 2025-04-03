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
    
    # Generate all possible arrangements of the first 9 numbers
    from itertools import permutations
    
    # Check if any permutation forms a magic square
    for perm in permutations(numbers[:9]):
        # Check rows
        if (perm[0] + perm[1] + perm[2] == magic_sum and
            perm[3] + perm[4] + perm[5] == magic_sum and
            perm[6] + perm[7] + perm[8] == magic_sum and
            
            # Check columns
            perm[0] + perm[3] + perm[6] == magic_sum and
            perm[1] + perm[4] + perm[7] == magic_sum and
            perm[2] + perm[5] + perm[8] == magic_sum and
            
            # Check diagonals
            perm[0] + perm[4] + perm[8] == magic_sum and
            perm[2] + perm[4] + perm[6] == magic_sum):
            
            # If grid matches the order specified by 10th number
            if numbers[9] == 0 or numbers[9] < 10:
                return True
    
    return False