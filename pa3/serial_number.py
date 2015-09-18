# Kevin Nash (kjn33)
# EECS 293
# Assignment 3

from fractions import gcd
from product_error import ProductError

class SerialNumber:
    """Store the serial number of an Orange product"""
        
    def __init__(self, serial_number):
        """Initialize the number attribute of this SerialNumber"""
        self.serial_number = serial_number

    def __cmp__(self, other):
        """Order SerialNumber objects in ascending order
        by their numerical values.
        """
        return cmp(self.serial_number, other.serial_number)

    def __str__(self):
        """Return the SerialNumber as a string"""
        return str(self.serial_number)

    def gcd(self, other):
        """Return the greatest common divisor of this SerialNumber
        and an other SerialNumber.
        """
        return gcd(self.serial_number, other.serial_number)

    def mod(self, other):
        """Return this SerialNumber modulus an other SerialNumber"""
        return self.serial_number % other.serial_number

    def test_bit(self, bit):
        """Return true iff a bit is set at the given index
        Example:
            12 is 0b1100
            Therefore given a SerialNumber of 12,
            test_bit returns false for indices 0 and 1
            test_bit returns true  for indices 2 and 3.
        """
        return (self.serial_number & (1 << bit) != 0)

    def is_zero(self):
        """Return true iff this SerialNumber is zero"""
        return self.serial_number == 0

    def is_even(self):
        """Return true iff this SerialNumber is even"""
        return not self.is_zero() and self.serial_number % 2 == 0

    def is_odd(self):
        """Return true iff this SerialNumber is odd"""
        return not self.is_zero() and not self.is_even()
