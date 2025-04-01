import logging
import pytest
from src.stack_trace_logger import log_stack_trace

class MockLogger:
    def __init__(self):
        self.logged_messages = []
        self.logged_levels = []

    def log(self, level, msg):
        self.logged_messages.append(msg)
        self.logged_levels.append(level)

def test_log_stack_trace_with_exception():
    mock_logger = MockLogger()
    try:
        raise ValueError("Test exception")
    except ValueError as e:
        stack_trace = log_stack_trace(e, logger=mock_logger)
        
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_levels[0] == logging.ERROR
    assert "ValueError: Test exception" in stack_trace
    assert "test_log_stack_trace_with_exception" in stack_trace

def test_log_stack_trace_current_stack():
    mock_logger = MockLogger()
    stack_trace = log_stack_trace(logger=mock_logger)
    
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_levels[0] == logging.ERROR
    assert "test_log_stack_trace_current_stack" in stack_trace

def test_log_stack_trace_custom_log_level():
    mock_logger = MockLogger()
    stack_trace = log_stack_trace(log_level=logging.WARNING, logger=mock_logger)
    
    assert len(mock_logger.logged_messages) == 1
    assert mock_logger.logged_levels[0] == logging.WARNING

def test_log_stack_trace_invalid_logger():
    with pytest.raises(TypeError, match="Invalid logger"):
        log_stack_trace(logger="not a logger")

def test_log_stack_trace_no_logger():
    # Test with root logger
    stack_trace = log_stack_trace()
    assert isinstance(stack_trace, str)
    assert len(stack_trace) > 0