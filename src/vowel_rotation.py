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
    vowel_sequences = {
        'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
        'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
    }
    
    # Use list comprehension to rotate vowels while preserving other characters
    return ''.join(vowel_sequences.get(char, char) for char in input_string)