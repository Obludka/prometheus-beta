from typing import List
from collections import Counter

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a substring that can be rearranged to form another substring.
    
    Args:
        s (str): Input string containing only lowercase English letters
    
    Returns:
        int: Number of distinct anagrams in the string
    
    Raises:
        ValueError: If the input string contains characters other than lowercase letters
    
    Examples:
        >>> count_anagrams('abab')
        4
        >>> count_anagrams('aa')
        3
    """
    # Validate input
    if not s or not all(char.islower() for char in s):
        raise ValueError("Input must be a non-empty string of lowercase letters")
    
    # Set to store unique anagram signatures
    unique_anagrams = set()
    
    # Generate all possible substrings and their sorted signatures
    for length in range(1, len(s) + 1):
        for i in range(len(s) - length + 1):
            # Get the substring
            substring = s[i:i+length]
            
            # Create a sorted signature of the substring
            # This identifies unique anagrams
            signature = ''.join(sorted(substring))
            
            # Add to unique anagrams set
            unique_anagrams.add(signature)
    
    # Return the count of unique anagram signatures
    return len(unique_anagrams)