# Kevin Nash (kjn33)
# EECS 293
# Assignment 2

class AbstractProduct:
    """TODO: add a docstring here"""

    def __init__(self, serial_number, product_name, description=None):
        """Initialize the attributes of this Product"""
        self.serial_number = serial_number
        self.description = description
        self.product_name = product_name

    def __eq__(self, other):
        """Override the natural equality check such that
        two Products are equal if they share the same serial number
        """
        return self.serial_number == other.serial_number

    def __hash__(self):
        """Override the natural hash value such that
        the hash of a product is determined by the serial number itself
        """
        return hash(self.serial_number.serial_number)

    def __str__(self):
        """ pass """
        out = "{name}: Serial #{serial}".format(name=self.product_name,
                                                serial=self.serial_number)
        if self.description:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out

