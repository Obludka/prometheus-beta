def generate_unique_permutations(input_string):
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        input_string (str): The string to generate permutations for.
    
    Returns:
        list: A list of unique permutations of the input string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return []
    
    # Use a set to ensure uniqueness
    unique_permutations = set()
    
    def backtrack(current_perm, remaining_chars):
        """
        Recursive helper function to generate permutations.
        
        Args:
            current_perm (str): Current permutation being built.
            remaining_chars (str): Remaining characters to permute.
        """
        # If no characters left, add the current permutation
        if not remaining_chars:
            unique_permutations.add(current_perm)
            return
        
        # Try each character as the next character in the permutation
        for i in range(len(remaining_chars)):
            # Choose current character
            next_char = remaining_chars[i]
            
            # Create new permutation and remaining characters
            new_perm = current_perm + next_char
            new_remaining = remaining_chars[:i] + remaining_chars[i+1:]
            
            # Recursively generate permutations
            backtrack(new_perm, new_remaining)
    
    # Start the backtracking process
    backtrack('', input_string)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))