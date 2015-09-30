# Kevin Nash (kjn33)
# EECS 293
# Assignment 4

from request import Request
from serial_number import SerialNumber

class Exchange(Request):
    """Handle requests to exchange products"""

    class Builder:
        """Set up the exchange"""

        compatible_products = set()

        def add_compatible(self, serial_number):
            """
            Add the serial number to the set of products
            compatible with the customer request
            """
            self.compatible_products.add(serial_number)
            return self

        def get_compatible_products(self):
            """Return the set of compatible products"""
            return set(self.compatible_products)

        def build(self):
            """
            Return an exchange with the given
            list of compatible products
            """
            return Exchange(self)

    def __init__(self, builder):
        """
        Create a new exchange with the list of
        compatible products provided by builder
        """
        self.compatible_products = builder.get_compatible_products()

    def get_compatible_products(self):
        """
        Return the serial numbers of the products
        compatible with the customer request
        """
        return set(self.compatible_products)
