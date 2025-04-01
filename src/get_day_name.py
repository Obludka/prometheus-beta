from datetime import datetime

def get_day_name(date):
    """
    Return the name of the day for a given date.

    Args:
        date (datetime or str): The date to get the day name for. 
                                If a string is provided, it should be in 'YYYY-MM-DD' format.

    Returns:
        str: The full name of the day (e.g., 'Monday', 'Tuesday', etc.)

    Raises:
        ValueError: If the input is not a valid date or cannot be parsed
    """
    # Convert input to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
    
    # Ensure input is a datetime object
    if not isinstance(date, datetime):
        raise ValueError("Input must be a datetime object or a date string in YYYY-MM-DD format")
    
    # Return the day name
    return date.strftime('%A')