import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_run_length_encode_basic():
    """Test basic RLE encoding scenarios."""
    assert run_length_encode("AABBBCCCC") == "2A3B4C"
    assert run_length_encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB") == "12W1B12W3B24W1B"

def test_run_length_decode_basic():
    """Test basic RLE decoding scenarios."""
    assert run_length_decode("2A3B4C") == "AABBBCCCC"
    assert run_length_decode("12W1B12W3B24W1B") == "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB"

def test_encode_decode_roundtrip():
    """Test that encoding and decoding preserves the original string."""
    test_strings = [
        "AABBBCCCC",
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB",
        "AAABBBCCCDDDEEE",
        "X" * 20,
        "ABCDEFG"
    ]
    
    for s in test_strings:
        assert run_length_decode(run_length_encode(s)) == s

def test_input_validation_encode():
    """Test input validation for encoding."""
    # Test non-string input
    with pytest.raises(TypeError):
        run_length_encode(123)
    
    # Test empty string
    with pytest.raises(ValueError):
        run_length_encode("")

def test_input_validation_decode():
    """Test input validation for decoding."""
    # Test non-string input
    with pytest.raises(TypeError):
        run_length_decode(123)
    
    # Test empty string
    with pytest.raises(ValueError):
        run_length_decode("")
    
    # Test invalid encoded string
    with pytest.raises(ValueError):
        run_length_decode("A")  # No count before character
    
    with pytest.raises(ValueError):
        run_length_decode("1A2")  # Incomplete encoding