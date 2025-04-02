def convert_to_alternating_header_case(input_string):
    """
    Convert a string to alternating header case.
    
    In alternating header case, every other word starts with a capital letter, 
    and the rest of the words are in lowercase.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating header case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_alternating_header_case("hello world python")
        'Hello world Python'
        >>> convert_to_alternating_header_case("PYTHON is AWESOME")
        'Python is awesome'
        >>> convert_to_alternating_header_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Split the string into words and strip extra whitespace
    words = input_string.lower().split()
    
    # Capitalize words at even indices (0-based)
    for i in range(0, len(words), 2):
        if words[i]:  # Ensure non-empty word
            words[i] = words[i].capitalize()
    
    # Join the words back together
    return ' '.join(words)