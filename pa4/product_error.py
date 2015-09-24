# Kevin Nash (kjn33)
# EECS 293
# Assignment 3

from enum import Enum

class ProductError(Exception):
    """Provide exceptions for product generation."""

    class ErrorCode(Enum):
        """Enumerate various error codes."""
        
        INVALID_SERIAL_NUMBER = 1
        INVALID_PRODUCT_TYPE = 2
        UNSUPPORTED_OPERATION = 3

    def __init__(self, product_type, serial_number, error_code):
        """Initialize the properties of a ProductError."""
        self.product_type = product_type
        self.product_name = product_type.value
        self.serial_number = serial_number
        self.error_code = error_code
