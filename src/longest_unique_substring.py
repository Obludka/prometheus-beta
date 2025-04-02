def longest_unique_substring(s: str) -> int:
    """
    Find the length of the longest substring with no repeated characters.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Length of the longest substring with unique characters
    
    Examples:
        >>> longest_unique_substring("abcabcbb")
        3
        >>> longest_unique_substring("bbbbb")
        1
        >>> longest_unique_substring("pwwkew")
        3
        >>> longest_unique_substring("")
        0
    """
    # Handle empty string case
    if not s:
        return 0
    
    # Use sliding window technique
    char_set = set()
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # If character is already in set, remove characters from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to set
        char_set.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length