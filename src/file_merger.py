"""
Module for merging multiple files into a single file.

This module provides functionality to combine multiple files 
into a single output file, with options for handling file contents.
"""

import os


def merge_files(input_files, output_file, separator='\n'):
    """
    Merge contents of multiple files into a single output file.

    Args:
        input_files (list): List of paths to input files to be merged.
        output_file (str): Path to the output merged file.
        separator (str, optional): String to use between file contents. 
                                   Defaults to newline.

    Raises:
        ValueError: If input_files is empty or contains non-existent files.
        IOError: If there are issues reading input files or writing output file.
    """
    # Validate input files
    if not input_files:
        raise ValueError("No input files provided")
    
    # Check that all input files exist
    non_existent_files = [f for f in input_files if not os.path.exists(f)]
    if non_existent_files:
        raise ValueError(f"The following files do not exist: {non_existent_files}")
    
    try:
        # Open output file in write mode
        with open(output_file, 'w') as outfile:
            # Iterate through input files
            for i, input_file in enumerate(input_files):
                # Read contents of each input file
                with open(input_file, 'r') as infile:
                    content = infile.read().strip()
                    
                    # Write content, add separator if not last file
                    outfile.write(content)
                    if i < len(input_files) - 1:
                        outfile.write(separator)
        
        return output_file
    except IOError as e:
        raise IOError(f"Error merging files: {e}")