# Kevin Nash (kjn33)
# EECS 293
# Assignment 4

from enum import Enum

class RequestError(Exception):
    """Provide exceptions for request processing"""

    class ErrorCode(Enum):
        """Enumerate various error codes"""
        
        INVALID_RMA = 1

    def __init__(self, error_code):
        """Initialize the properties of a ProductError"""
        self.error_code = error_code
