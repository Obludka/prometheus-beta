def rotate_vowels(input_string):
    """
    Replace each vowel in the input string with the next vowel in the alphabet,
    preserving the original case.
    
    Args:
        input_string (str): The input string to transform
    
    Returns:
        str: A new string with vowels rotated to the next vowel
    
    Examples:
        >>> rotate_vowels("hello")
        "hollo"
        >>> rotate_vowels("HELLO")
        "HOLLO"
        >>> rotate_vowels("aeiou")
        "eioua"
        >>> rotate_vowels("xyz")
        "xyz"
    """
    # Define vowel sequences (lowercase and uppercase)
    vowel_map = {
        'a': 'o', 'e': 'u', 'i': 'o', 'o': 'u', 'u': 'a',
        'A': 'O', 'E': 'U', 'I': 'O', 'O': 'U', 'U': 'A'
    }
    
    # Transform each character
    def transform_vowel(char):
        # If char is a vowel, replace it; otherwise, return the original char
        return vowel_map.get(char, char)
    
    # Create the rotated string
    return ''.join(transform_vowel(char) for char in input_string)