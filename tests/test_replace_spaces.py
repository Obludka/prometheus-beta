import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_replace_spaces_basic():
    """Test basic space replacement."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_multiple():
    """Test replacing multiple spaces."""
    assert replace_spaces_with_underscores("hello  world  test") == "hello__world__test"

def test_replace_spaces_edges():
    """Test spaces at the beginning and end of string."""
    assert replace_spaces_with_underscores("  spaces at edges  ") == "__spaces_at_edges__"

def test_empty_string():
    """Test empty string input."""
    assert replace_spaces_with_underscores("") == ""

def test_no_spaces():
    """Test string with no spaces."""
    assert replace_spaces_with_underscores("nospaceshere") == "nospaceshere"

def test_none_input():
    """Test None input handling."""
    assert replace_spaces_with_underscores(None) == ""

def test_only_spaces():
    """Test string containing only spaces."""
    assert replace_spaces_with_underscores("   ") == "___"