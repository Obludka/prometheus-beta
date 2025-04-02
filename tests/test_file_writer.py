"""
Tests for the file_writer module.
"""

import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file_basic(tmp_path):
    """Test basic string writing to a file."""
    test_file = tmp_path / "test_write.txt"
    test_content = "Hello, World!"
    
    write_string_to_file(str(test_file), test_content)
    
    with open(test_file, 'r') as file:
        assert file.read() == test_content

def test_write_string_to_file_append(tmp_path):
    """Test appending to a file."""
    test_file = tmp_path / "test_append.txt"
    
    # First write
    write_string_to_file(str(test_file), "First line\n")
    
    # Append
    write_string_to_file(str(test_file), "Second line\n", mode='a')
    
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "First line\n" + "Second line\n"

def test_write_string_to_file_invalid_path():
    """Test invalid file path raises appropriate error."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "Some content")

def test_write_string_to_file_invalid_types():
    """Test type checking for inputs."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "Some content")
    
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_non_existent_directory(tmp_path):
    """Test writing to a file in a non-existent directory."""
    non_existent_dir = tmp_path / "non_existent_dir"
    test_file = non_existent_dir / "test.txt"
    
    with pytest.raises(IOError):
        write_string_to_file(str(test_file), "Some content")

def test_write_string_to_file_with_special_characters(tmp_path):
    """Test writing a string with special characters."""
    test_file = tmp_path / "special_chars.txt"
    test_content = "Line with special chars: !@#$%^&*()_+"
    
    write_string_to_file(str(test_file), test_content)
    
    with open(test_file, 'r') as file:
        assert file.read() == test_content

def test_write_string_to_file_unicode(tmp_path):
    """Test writing unicode characters."""
    test_file = tmp_path / "unicode.txt"
    test_content = "こんにちは World! 🌍"
    
    write_string_to_file(str(test_file), test_content)
    
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == test_content