import logging

def log_length(item):
    """
    Log the length of a string or array/list.

    Args:
        item (str or list or tuple): The input to measure length of.

    Returns:
        int: The length of the input.

    Raises:
        TypeError: If the input is not a string, list, or tuple.
    """
    # Validate input type
    if not isinstance(item, (str, list, tuple)):
        raise TypeError("Input must be a string, list, or tuple")

    # Calculate length
    length = len(item)

    # Log the length 
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(f"Length: {length}")

    return length