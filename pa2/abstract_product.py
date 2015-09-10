# Kevin Nash (kjn33)
# EECS 293
# Assignment 2

import abc

class AbstractProduct:
    """Represent an Orange product"""

    __metaclass__ = abc.ABCMeta

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Product"""
        self.serial_number = serial_number
        self.description = description

    def __eq__(self, other):
        """Override the natural equality check such that
        two Products are equal if they share the same serial number.
        """
        return self.serial_number == other.serial_number

    def __hash__(self):
        """Override the natural hash value such that
        the hash of a product is determined by the serial number itself.
        """
        return hash(self.serial_number.serial_number)

    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError
