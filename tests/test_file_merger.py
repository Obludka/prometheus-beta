"""
Test suite for file_merger module.

This module contains comprehensive tests for the merge_files function,
covering various scenarios and edge cases.
"""

import os
import pytest
import tempfile

from src.file_merger import merge_files


def test_merge_files_basic():
    """Test basic file merging functionality."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1_path, 'w') as f1:
            f1.write("Hello")
        with open(file2_path, 'w') as f2:
            f2.write("World")
        
        # Merge files
        merged_file = merge_files([file1_path, file2_path], output_path)
        
        # Check output
        with open(merged_file, 'r') as merged:
            content = merged.read()
            assert content == "HelloWorld"


def test_merge_files_with_separator():
    """Test file merging with custom separator."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        file1_path = os.path.join(tmpdir, 'file1.txt')
        file2_path = os.path.join(tmpdir, 'file2.txt')
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        with open(file1_path, 'w') as f1:
            f1.write("Hello")
        with open(file2_path, 'w') as f2:
            f2.write("World")
        
        # Merge files with custom separator
        merged_file = merge_files([file1_path, file2_path], output_path, separator=' ')
        
        # Check output
        with open(merged_file, 'r') as merged:
            content = merged.read()
            assert content == "Hello World"


def test_merge_files_empty_input():
    """Test merging with empty input list raises ValueError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        with pytest.raises(ValueError, match="No input files provided"):
            merge_files([], output_path)


def test_merge_files_nonexistent_files():
    """Test merging with nonexistent files raises ValueError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        with pytest.raises(ValueError, match="do not exist"):
            merge_files(['/path/to/nonexistent/file1.txt', '/path/to/nonexistent/file2.txt'], output_path)


def test_merge_files_single_file():
    """Test merging a single file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input file
        file_path = os.path.join(tmpdir, 'file.txt')
        output_path = os.path.join(tmpdir, 'merged.txt')
        
        with open(file_path, 'w') as f:
            f.write("Single file content")
        
        # Merge single file
        merged_file = merge_files([file_path], output_path)
        
        # Check output
        with open(merged_file, 'r') as merged:
            content = merged.read()
            assert content == "Single file content"