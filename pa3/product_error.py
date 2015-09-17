# Kevin Nash (kjn33)
# EECS 293
# Assignment 3

from enum import Enum

class ProductError(Exception):
    """"""

    class ErrorCode(Enum):
        """"""
        INVALID_SERIAL_NUMBER = 1
        INVALID_PRODUCT_TYPE = 2
        UNSUPPORTED_OPERATION = 3

    def __init__(self, product_type, serial_number, error_code):
        """"""
        self.product_type = product_type
        self.serial_number = serial_number
        self.error_code = error_code
