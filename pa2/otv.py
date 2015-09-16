# Kevin Nash (kjn33)
# EECS 293
# Assignment 2

from abstract_product import AbstractProduct
from product_type import ProductType

class Opod(AbstractProduct):
    """Represent an oPod"""

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Opod"""
        AbstractProduct.__init__(self, serial_number, description)
        self.product_type = ProductType.OPOD
        self.product_name = ProductType.OPOD.__str__()

    def __str__(self):
        """Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable.
        """
        out = "{name}: Serial #{serial}".format(name=self.product_name,
                                                serial=self.serial_number)
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out

    @staticmethod
    def is_valid_serial_number(serial_number):
        """Return true iff the serial number is odd and
        its greatest common denominator with 620 is less than or equal to 14
        """
        return serial_number.is_odd() and
               serial_number.gcd(SerialNumber(630)) < 14