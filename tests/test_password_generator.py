import pytest
import string
from src.password_generator import generate_password

def test_password_length():
    """Test that generated password matches the specified length."""
    for length in [4, 8, 12, 16, 32]:
        password = generate_password(length)
        assert len(password) == length

def test_password_complexity():
    """Test that password contains characters from all character sets."""
    password = generate_password(12)
    
    # Check that password contains at least one character from each set
    assert any(char in string.ascii_lowercase for char in password)
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)

def test_randomness():
    """Test that multiple generated passwords are not identical."""
    passwords = set(generate_password(10) for _ in range(100))
    assert len(passwords) > 1

def test_invalid_length_inputs():
    """Test error handling for invalid length inputs."""
    with pytest.raises(TypeError):
        generate_password("10")
    
    with pytest.raises(ValueError):
        generate_password(0)
    
    with pytest.raises(ValueError):
        generate_password(-5)

def test_minimum_length():
    """Test generating a password of minimum length (1)."""
    password = generate_password(1)
    assert len(password) == 1
    assert password  # Ensure not an empty string