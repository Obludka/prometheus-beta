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
    dictionary = {}
    compressed = bytearray()
    current_phrase = bytes()
    
    # Compression process
    for byte in input_data:
        # Extend current phrase
        current_phrase += bytes([byte])
        
        # If phrase is not in dictionary, add it
        if current_phrase not in dictionary:
            # Add entry to dictionary
            dictionary[current_phrase] = len(dictionary)
            
            # If longer than one byte, output previous phrase
            if len(current_phrase) > 1:
                compressed.extend(_encode_phrase(current_phrase[:-1], dictionary))
            
            # Reset current phrase to last byte
            current_phrase = bytes([byte])
    
    # Add final phrase
    if current_phrase:
        compressed.extend(_encode_phrase(current_phrase, dictionary))
    
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

    # Initialize data structures
    dictionary = {}
    decompressed = bytearray()
    
    # Decompression process
    i = 0
    while i < len(compressed_data):
        # Extract length and phrase
        length, phrase = _decode_phrase(compressed_data[i:])
        
        # Add phrase to decompressed data
        decompressed.extend(phrase)
        
        # Add to dictionary
        dictionary[len(dictionary)] = phrase
        
        # Move to next compressed chunk
        i += len(phrase) + 1  # +1 for length byte
    
    return bytes(decompressed)

def _encode_phrase(phrase, dictionary):
    """
    Encode a phrase by finding its dictionary index.

    Args:
        phrase (bytes): Phrase to encode
        dictionary (dict): Compression dictionary

    Returns:
        bytes: Encoded representation of the phrase
    """
    # Find the index of the phrase in dictionary
    index = dictionary.get(phrase, -1)
    
    # If phrase not found, return direct bytes
    if index == -1:
        return bytes([len(phrase)]) + phrase
    
    # Return encoded index
    return bytes([index])

def _decode_phrase(compressed_chunk):
    """
    Decode a compressed chunk.

    Args:
        compressed_chunk (bytes): Chunk of compressed data

    Returns:
        tuple: (length, decoded_phrase)
    """
    # If chunk is empty, return empty result
    if not compressed_chunk:
        return 0, bytes()
    
    # If first byte is less than dictionary size, it's a dictionary reference
    if compressed_chunk[0] < 256:  # Assuming max dictionary size
        return 1, bytes([compressed_chunk[0]])
    
    # Otherwise, it's a literal phrase
    length = compressed_chunk[0]
    phrase = compressed_chunk[1:length+1]
    return length + 1, phrase