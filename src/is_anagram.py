def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. This implementation is case-insensitive 
    and ignores whitespace.

    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Raises:
        TypeError: If either input is not a string
    """
    # Check input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both arguments must be strings")

    # Remove whitespace and convert to lowercase
    cleaned_str1 = str1.replace(" ", "").lower()
    cleaned_str2 = str2.replace(" ", "").lower()

    # Quick length check 
    if len(cleaned_str1) != len(cleaned_str2):
        return False

    # Use character frequency counting
    char_count = {}

    # Count characters in first string
    for char in cleaned_str1:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract characters from second string
    for char in cleaned_str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True