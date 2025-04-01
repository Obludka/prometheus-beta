def replace_spaces_with_underscores(input_string: str) -> str:
    """
    Replace all spaces in a given string with underscores.

    Args:
        input_string (str): The input string to modify.

    Returns:
        str: A new string with all spaces replaced by underscores.

    Examples:
        >>> replace_spaces_with_underscores("hello world")
        'hello_world'
        >>> replace_spaces_with_underscores("  spaces  at  edges  ")
        '__spaces__at__edges__'
        >>> replace_spaces_with_underscores("")
        ''
    """
    # Handle None input
    if input_string is None:
        return ""
    
    # Replace spaces with underscores
    return input_string.replace(" ", "_")