import traceback
import logging
import sys
from typing import Optional, Union, Callable, Any

def log_stack_trace(
    exception: Optional[Union[Exception, BaseException]] = None, 
    log_level: int = logging.ERROR, 
    logger: Optional[Union[logging.Logger, object]] = None
) -> str:
    """
    Log a stack trace from an exception or the current stack trace.

    Args:
        exception (Optional[Exception]): The exception to log. 
            If None, logs the current stack trace.
        log_level (int): Logging level (default is logging.ERROR)
        logger (Optional[Union[Logger, object]]): Custom logger. 
            If None, uses the root logger.

    Returns:
        str: The formatted stack trace as a string

    Raises:
        TypeError: If an invalid logger is provided
    """
    # Use root logger if no logger is specified
    if logger is None:
        logger = logging.getLogger()

    # Check if logger has required logging method
    if not hasattr(logger, 'log'):
        raise TypeError("Invalid logger. Must have a 'log' method")

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