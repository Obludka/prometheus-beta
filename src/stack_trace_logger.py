import traceback
import logging
import sys
from typing import Optional, Union, Callable, Any

def log_stack_trace(
    exception: Optional[Union[Exception, BaseException]] = None, 
    log_level: int = logging.ERROR, 
    logger: Optional[logging.Logger] = None
) -> str:
    """
    Log a stack trace from an exception or the current stack trace.

    Args:
        exception (Optional[Exception]): The exception to log. 
            If None, logs the current stack trace.
        log_level (int): Logging level (default is logging.ERROR)
        logger (Optional[logging.Logger]): Custom logger. 
            If None, uses the root logger.

    Returns:
        str: The formatted stack trace as a string

    Raises:
        TypeError: If an invalid logger is provided
    """
    # Use root logger if no logger is specified
    if logger is None:
        logger = logging.getLogger()

    # Validate logger
    if not isinstance(logger, logging.Logger):
        raise TypeError("Invalid logger. Must be an instance of logging.Logger")

    # Get stack trace string
    if exception is not None:
        # If an exception is provided, use its traceback
        stack_trace = ''.join(traceback.format_exception(
            type(exception), exception, exception.__traceback__
        ))
    else:
        # If no exception, get current stack trace
        stack_trace = ''.join(traceback.format_stack())

    # Log the stack trace
    logger.log(log_level, stack_trace)

    return stack_trace