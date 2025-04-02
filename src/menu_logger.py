import logging
import os
from typing import List, Any, Optional

class MenuLogger:
    """
    A class to log user selections from a menu with various logging capabilities.
    
    Attributes:
        log_file (Optional[str]): Path to the log file. If None, uses default logging.
    """
    
    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize the MenuLogger.
        
        Args:
            log_file (Optional[str], optional): Path to the log file for storing selections. 
                                                Defaults to None.
        """
        # Ensure log directory exists if log_file is specified
        if log_file:
            os.makedirs(os.path.dirname(os.path.abspath(log_file)) or '.', exist_ok=True)
        
        # Remove any existing loggers to prevent duplicate logging
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=log_file,
            filemode='w'  # Write mode to start fresh each time
        )
        self.logger = logging.getLogger(__name__)
    
    def log_selection(self, menu_name: str, selection: Any) -> None:
        """
        Log a user's menu selection.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selection (Any): The selected item from the menu.
        
        Raises:
            ValueError: If menu_name is empty or None.
        """
        # Validate inputs
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        # Log the selection
        log_message = f"Menu '{menu_name}' - Selected: {selection}"
        self.logger.info(log_message)
    
    def log_multiple_selections(self, menu_name: str, selections: List[Any]) -> None:
        """
        Log multiple selections from a menu.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selections (List[Any]): List of selected items.
        
        Raises:
            ValueError: If menu_name is empty or selections is empty.
        """
        # Validate inputs
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        if not selections:
            raise ValueError("Selections list cannot be empty")
        
        # Log multiple selections
        log_message = f"Menu '{menu_name}' - Selections: {', '.join(str(s) for s in selections)}"
        self.logger.info(log_message)