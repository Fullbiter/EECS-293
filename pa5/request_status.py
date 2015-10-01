# Kevin Nash (kjn33)
# EECS 293
# Assignment 4

from enum import Enum

class RequestStatus(Exception):
    """Provide exceptions for product generation."""

    class StatusCode(Enum):
        """Enumerate various request states."""
        
        OK = 0
        UNKNOWN = 1
        FAIL = 2

    def __init__(self):
        """Initialize the properties of a ProductError."""
        self.status_code = RequestStatus.StatusCode.UNKNOWN
        self.result = None
