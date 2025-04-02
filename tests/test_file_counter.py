import os
import pytest
import tempfile
import shutil

from src.file_counter import count_files_in_directory

def test_count_files_in_empty_directory():
    """Test counting files in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert count_files_in_directory(temp_dir) == 0

def test_count_files_in_non_empty_directory():
    """Test counting files in a directory with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        for i in range(5):
            open(os.path.join(temp_dir, f'test_file_{i}.txt'), 'w').close()
        
        assert count_files_in_directory(temp_dir) == 5

def test_count_files_ignores_subdirectories():
    """Test that subdirectories are not counted as files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files and a subdirectory
        for i in range(3):
            open(os.path.join(temp_dir, f'test_file_{i}.txt'), 'w').close()
        os.mkdir(os.path.join(temp_dir, 'test_subdir'))
        
        assert count_files_in_directory(temp_dir) == 3

def test_non_existent_directory():
    """Test that FileNotFoundError is raised for non-existent directory."""
    with pytest.raises(FileNotFoundError):
        count_files_in_directory('/path/to/non/existent/directory')

def test_not_a_directory():
    """Test that NotADirectoryError is raised when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            count_files_in_directory(temp_file.name)

# Note: The PermissionError test is complex to simulate reliably across systems,
# so it's omitted for cross-platform compatibility