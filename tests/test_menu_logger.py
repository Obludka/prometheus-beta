import os
import logging
import pytest
from src.menu_logger import MenuLogger

def test_single_selection_logging(tmp_path):
    """Test logging a single menu selection."""
    log_file = tmp_path / "menu_log.txt"
    # Explicitly create the file before logging
    log_file.touch()
    logger = MenuLogger(str(log_file))
    
    # Log a selection
    logger.log_selection("Main Menu", "Option 1")
    
    # Verify log content
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Menu 'Main Menu' - Selected: Option 1" in log_content

def test_multiple_selections_logging(tmp_path):
    """Test logging multiple menu selections."""
    log_file = tmp_path / "menu_log.txt"
    # Explicitly create the file before logging
    log_file.touch()
    logger = MenuLogger(str(log_file))
    
    # Log multiple selections
    logger.log_multiple_selections("Settings Menu", ["Dark Mode", "Notifications"])
    
    # Verify log content
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Menu 'Settings Menu' - Selections: Dark Mode, Notifications" in log_content

def test_empty_menu_name_raises_error():
    """Test that empty menu name raises ValueError."""
    logger = MenuLogger()
    
    with pytest.raises(ValueError, match="Menu name cannot be empty"):
        logger.log_selection("", "Option")
    
    with pytest.raises(ValueError, match="Menu name cannot be empty"):
        logger.log_multiple_selections("", ["Option 1", "Option 2"])

def test_empty_selections_raises_error():
    """Test that empty selections list raises ValueError."""
    logger = MenuLogger()
    
    with pytest.raises(ValueError, match="Selections list cannot be empty"):
        logger.log_multiple_selections("Menu", [])

def test_different_selection_types(tmp_path):
    """Test logging selections of different types."""
    log_file = tmp_path / "menu_log.txt"
    # Explicitly create the file before logging
    log_file.touch()
    logger = MenuLogger(str(log_file))
    
    # Log selections of different types
    logger.log_selection("Number Menu", 42)
    logger.log_selection("Boolean Menu", True)
    logger.log_multiple_selections("Mixed Menu", [1, "text", False])
    
    # Verify log content
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Menu 'Number Menu' - Selected: 42" in log_content
        assert "Menu 'Boolean Menu' - Selected: True" in log_content
        assert "Menu 'Mixed Menu' - Selections: 1, text, False" in log_content

def test_default_logging():
    """Test logging without a specific log file."""
    logger = MenuLogger()
    
    # Verify no exception is raised
    try:
        logger.log_selection("Test Menu", "Option")
        logger.log_multiple_selections("Another Menu", ["Option 1", "Option 2"])
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")