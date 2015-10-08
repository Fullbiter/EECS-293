# Kevin Nash (kjn33)
# EECS 293
# Assignment 5

import abc
from request_error import RequestError
from request_status import RequestStatus
from serial_number import SerialNumber

class Request(object):
    """Function like an interface"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        """Enforce the abstract quality of Request"""
        raise NotImplementedError("class Request cannot be instantiated")

    def process(self, product, status):
        """Call upon the product for processing"""
        product.process(self, status)

class Exchange(Request):
    """Handle requests to exchange products"""

    class Builder:
        """Set up the Exchange"""

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

class Refund(Request):
    """Handle requests to refund products"""

    class Builder:
        """Set up the Refund"""

        def set_rma(self, rma):
            """
            Add the serial number to the set of products
            compatible with the customer request
            """
            if rma is None:
                raise RequestError(RequestError.ErrorCode.INVALID_RMA)
            self.rma = rma
            return self

        def build(self):
            """
            Return an Refund with the given
            list of compatible products
            """
            return Refund(self)

    def __init__(self, builder):
        """
        Create a new Refund with the list of
        compatible products provided by builder
        """
        self.rma = builder.rma
