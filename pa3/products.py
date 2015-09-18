# Kevin Nash (kjn33)
# EECS 293
# Assignment 3

import abc
from product_error import ProductError
from product_type import ProductType
from serial_number import SerialNumber

class AbstractProduct(object):
    """Represent any Orange product"""

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

    def __ne__(self, other):
        """Override the natural equality check such that two Products are
        not equal if they do not share the same serial number.
        """
        return not __eq__(self, other)

    def __hash__(self):
        """Override the natural hash value such that
        the hash of a product is determined by the serial number itself.
        """
        return hash(self.serial_number.serial_number)

    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError

    
    @staticmethod
    def make(product_type, serial_number, description=None):
        """"""
        # length of the name of the enum (e.g. ProductType is 11 chars long)
        enum_name_length = len(str(product_type.__class__.__name__))
        
        # the class associated with the product type
        product_class = eval(str(product_type) \
                        [enum_name_length + 1:].lower().capitalize())

        if product_class.is_valid_serial_number(serial_number):
            return product_class(serial_number, description)
        raise ProductError(product_type, serial_number,
                           ProductError.ErrorCode.INVALID_SERIAL_NUMBER)

class Opod(AbstractProduct):
    """Represent an oPod"""

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Opod"""
        AbstractProduct.__init__(self, serial_number, description)
        self.product_type = ProductType.OPOD
        self.product_name = str(ProductType.OPOD)

    def __str__(self):
        """Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable.
        """
        out = "{name}: Serial #{serial}".format(name=str(self.product_name),
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out

    @staticmethod
    def is_valid_serial_number(serial_number):
        """Return true iff the serial number is even
        and its third bit is not set.
        """
        return serial_number.is_even() and not serial_number.test_bit(2)

class Opad(AbstractProduct):
    """Represent an oPad"""

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Opad"""
        AbstractProduct.__init__(self, serial_number, description)
        self.product_type = ProductType.OPAD
        self.product_name = str(ProductType.OPAD)

    def __str__(self):
        """Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable.
        """
        out = "{name}: Serial #{serial}".format(name=str(self.product_name),
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out

    @staticmethod
    def is_valid_serial_number(serial_number):
        """Return true iff the serial number is even
        and its third bit is not set.
        """
        return serial_number.is_even() and serial_number.test_bit(2)

class Ophone(AbstractProduct):
    """Represent an oPhone"""

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Ophone"""
        AbstractProduct.__init__(self, serial_number, description)
        self.product_type = ProductType.OPHONE
        self.product_name = str(ProductType.OPHONE)

    def __str__(self):
        """Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable.
        """
        out = "{name}: Serial #{serial}".format(name=str(self.product_name),
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out

    @staticmethod
    def is_valid_serial_number(serial_number):
        """Return true iff the serial number is odd and
        its greatest common denominator with 620 is greater than 42
        """
        return serial_number.is_odd() and \
               serial_number.gcd(SerialNumber(630)) > 42

class Owatch(AbstractProduct):
    """Represent an oWatch"""

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Opod"""
        AbstractProduct.__init__(self, serial_number, description)
        self.product_type = ProductType.OWATCH
        self.product_name = str(ProductType.OWATCH)

    def __str__(self):
        """Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable.
        """
        out = "{name}: Serial #{serial}".format(name=str(self.product_name),
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out

    @staticmethod
    def is_valid_serial_number(serial_number):
        """Return true iff the serial number is odd
        and its greatest common denominator with 620 is above 14
        and less than or equal to 42.
        """
        return serial_number.is_odd() and \
               14 < serial_number.gcd(SerialNumber(630)) <= 42
               
class Otv(AbstractProduct):
    """Represent an oTv"""

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Otv"""
        AbstractProduct.__init__(self, serial_number, description)
        self.product_type = ProductType.OTV
        self.product_name = str(ProductType.OTV)

    def __str__(self):
        """Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable.
        """
        out = "{name}: Serial #{serial}".format(name=str(self.product_name),
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out

    @staticmethod
    def is_valid_serial_number(serial_number):
        """Return true iff the serial number is odd and
        its greatest common denominator with 620 is less than or equal to 14
        """
        return serial_number.is_odd() and \
               serial_number.gcd(SerialNumber(630)) < 14
