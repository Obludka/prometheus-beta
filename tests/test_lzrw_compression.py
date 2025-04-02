"""
Tests for LZRW Compression Algorithm

This module provides comprehensive tests for the LZRW compression 
and decompression functions.
"""

import pytest
import random
from src.lzrw_compression import compress, decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of simple string."""
    original = b"Hello, World!"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original

def test_empty_input():
    """Test compression and decompression of empty input."""
    original = b""
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original

def test_repeated_patterns():
    """Test compression of data with repeated patterns."""
    original = b"AAAABBBBCCCCDDDD"
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original

def test_random_bytes():
    """Test compression with random byte sequences."""
    # Generate random bytes
    random.seed(42)  # For reproducibility
    original = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = compress(original)
    decompressed = decompress(compressed)
    assert decompressed == original

def test_error_handling_non_bytes_input():
    """Test that TypeError is raised for non-bytes input."""
    with pytest.raises(TypeError):
        compress("Not bytes")
    
    with pytest.raises(TypeError):
        decompress("Not bytes")

def test_various_input_sizes():
    """Test compression with different input sizes."""
    test_cases = [
        b"a",  # Single byte
        b"ab" * 100,  # Short repeated sequence
        b"x" * 1000,  # Long repeated sequence
        bytes(range(256))  # All possible byte values
    ]
    
    for original in test_cases:
        compressed = compress(original)
        decompressed = decompress(compressed)
        assert decompressed == original, f"Failed for input of length {len(original)}"

def test_edge_cases():
    """Test various edge case inputs."""
    edge_cases = [
        b'\x00' * 100,  # Null bytes
        b'\xFF' * 100,  # Max byte value
        bytes(range(100))  # Sequentially increasing bytes
    ]
    
    for original in edge_cases:
        compressed = compress(original)
        decompressed = decompress(compressed)
        assert decompressed == original, f"Failed for edge case: {original}"