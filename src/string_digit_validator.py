def is_digits_only(s: str) -> bool:
    """
    Check if a string contains only digits.

    Args:
        s (str): The input string to validate.

    Returns:
        bool: True if the string contains only digits, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Check if string is empty
    if len(s) == 0:
        return False
    
    # Use string method to check if all characters are digits
    return s.isdigit()