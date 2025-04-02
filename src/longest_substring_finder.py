def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    Args:
        s (str): Input string to search for the longest unique substring.
    
    Returns:
        str: The longest substring without repeating characters.
             If multiple such substrings exist, returns the first one.
    
    Notes:
        - The function is case-sensitive
        - If the input is an empty string, returns an empty string
    
    Examples:
        >>> find_longest_substring("abcabcbb")
        'abc'
        >>> find_longest_substring("bbbbb")
        'b'
        >>> find_longest_substring("pwwkew")
        'wke'
    """
    # Handle empty string case
    if not s:
        return ""
    
    # Initialize variables to track the longest substring
    longest_substring = ""
    current_substring = ""
    
    for char in s:
        # If character is not in current substring, add it
        if char not in current_substring:
            current_substring += char
        else:
            # If character is a repeat, reset substring from after first repeat
            repeat_index = current_substring.index(char)
            current_substring = current_substring[repeat_index+1:] + char
        
        # Update longest substring if current is longer
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    return longest_substring