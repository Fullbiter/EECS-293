# Kevin Nash (kjn33)
# EECS 293
# Assignment 4

from request import Request
from request_error import RequestError

class Refund(Request):
    """Handle requests to exchange products"""

    class Builder:
        """Set up the exchange"""

        compatible_products = set()

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
            Return an exchange with the given
            list of compatible products
            """
            return Refund(self)

    def __init__(self, builder):
        """
        Create a new exchange with the list of
        compatible products provided by builder
        """
        self.rma = builder.rma
