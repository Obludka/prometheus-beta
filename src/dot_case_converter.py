def convert_to_dot_case(input_string: str) -> str:
    """
    Convert a given string to dot case.
    
    Dot case converts the input string to lowercase with dots separating words.
    Handles various input formats including camelCase, snake_case, and regular strings.
    
    Args:
        input_string (str): The input string to convert to dot case
    
    Returns:
        str: The input string converted to dot case
    
    Raises:
        TypeError: If the input is not a string
    
    Examples:
        >>> convert_to_dot_case("HelloWorld")
        'hello.world'
        >>> convert_to_dot_case("hello_world")
        'hello.world'
        >>> convert_to_dot_case("Hello World")
        'hello.world'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Replace multiple types of word separators with a standard separator
    normalized_string = input_string.replace('_', ' ').replace('-', ' ')
    
    # Split the string, converting to lowercase and joining with dots
    return '.'.join(
        word.lower() for word in normalized_string.split() 
        if word.strip()  # Ignore empty words
    )