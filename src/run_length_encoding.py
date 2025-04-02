def run_length_encode(input_string):
    """
    Implement Run-Length Encoding (RLE) for data compression.
    
    Args:
        input_string (str): The input string to be compressed.
    
    Returns:
        str: The run-length encoded string.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is empty.
    
    Examples:
        >>> run_length_encode("AABBBCCCC")
        '2A3B4C'
        >>> run_length_encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB")
        '12W1B12W3B24W1B'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Perform Run-Length Encoding
    encoded = []
    count = 1
    current_char = input_string[0]
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    
    # Add the last group
    encoded.append(str(count) + current_char)
    
    return ''.join(encoded)

def run_length_decode(encoded_string):
    """
    Decode a Run-Length Encoded string.
    
    Args:
        encoded_string (str): The run-length encoded string to be decoded.
    
    Returns:
        str: The original decoded string.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input string is invalid or cannot be decoded.
    
    Examples:
        >>> run_length_decode('2A3B4C')
        'AABBBCCCC'
        >>> run_length_decode('12W1B12W3B24W1B')
        'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB'
    """
    # Validate input
    if not isinstance(encoded_string, str):
        raise TypeError("Input must be a string")
    
    if not encoded_string:
        raise ValueError("Input string cannot be empty")
    
    # Perform Run-Length Decoding
    decoded = []
    count_str = ''
    
    for char in encoded_string:
        if char.isdigit():
            count_str += char
        else:
            if not count_str:
                raise ValueError(f"Invalid encoded string: {encoded_string}")
            
            decoded.append(int(count_str) * char)
            count_str = ''
    
    return ''.join(decoded)