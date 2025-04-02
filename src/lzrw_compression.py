"""
LZRW Compression Algorithm Implementation

This module provides a basic implementation of the LZRW (Lempel-Ziv Ross Williams) 
compression algorithm, which is a fast dictionary-based compression technique.

References:
- Original algorithm by Ross Williams
"""

def compress(input_data):
    """
    Compress input data using LZRW compression algorithm.

    Args:
        input_data (bytes): The input data to be compressed.

    Returns:
        bytes: Compressed data.

    Raises:
        TypeError: If input is not bytes.
    """
    # Input validation
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not input_data:
        return bytes()

    # Initialize data structures
    compressed = bytearray()
    
    # Simple copy if not much to compress
    if len(input_data) <= 2:
        compressed.append(0)  # Flag byte for uncompressed
        compressed.extend(input_data)
        return bytes(compressed)

    # Initialize dictionary and state
    dictionary = {}
    match_found = False
    i = 0

    while i < len(input_data):
        # Try to find the longest match
        longest_match_length = 0
        longest_match_offset = 0

        # Sliding window to search for matches
        for j in range(max(0, i - 255), i):
            # Check current and following bytes
            current_match_length = 0
            while (i + current_match_length < len(input_data) and 
                   input_data[j + current_match_length] == input_data[i + current_match_length]):
                current_match_length += 1
                
                # Ensure we don't go out of bounds
                if j + current_match_length >= i or i + current_match_length >= len(input_data):
                    break

            # Update longest match if necessary
            if current_match_length > longest_match_length:
                longest_match_length = current_match_length
                longest_match_offset = i - j

        # Decide how to encode
        if longest_match_length > 2:
            # Encode match (offset, length)
            compressed.append(longest_match_offset)
            compressed.append(longest_match_length)
            match_found = True
            i += longest_match_length
        else:
            # Encode literal byte
            compressed.append(0)  # Flag for literal
            compressed.append(input_data[i])
            i += 1

    return bytes(compressed)

def decompress(compressed_data):
    """
    Decompress data compressed with LZRW algorithm.

    Args:
        compressed_data (bytes): The compressed input data.

    Returns:
        bytes: Decompressed original data.

    Raises:
        TypeError: If input is not bytes.
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not compressed_data:
        return bytes()

    # If very short, return as-is
    if len(compressed_data) <= 2:
        return compressed_data[1:] if compressed_data[0] == 0 else compressed_data

    # Initialize decompression
    decompressed = bytearray()
    i = 0

    while i < len(compressed_data):
        # Check if it's a literal or a match
        if compressed_data[i] == 0:
            # Literal byte
            if i + 1 < len(compressed_data):
                decompressed.append(compressed_data[i + 1])
                i += 2
            else:
                break
        else:
            # Match (offset, length)
            if i + 1 < len(compressed_data):
                offset = compressed_data[i]
                length = compressed_data[i + 1]
                
                # Ensure offset doesn't go out of bounds
                start = max(0, len(decompressed) - offset)
                
                # Repeat bytes from previous parts of decompressed data
                for j in range(length):
                    if start + j < len(decompressed):
                        decompressed.append(decompressed[start + j])
                    else:
                        break
                
                i += 2
            else:
                break

    return bytes(decompressed)