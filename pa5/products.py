# Kevin Nash (kjn33)
# EECS 293
# Assignment 4

import abc
from product_error import ProductError
from product_type import ProductType
from requests import Exchange
from requests import Refund
from request_status import RequestStatus
from serial_number import SerialNumber

class AbstractProduct(object):
    """Represent any Orange product"""

    __metaclass__ = abc.ABCMeta

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Product"""
        self.serial_number = serial_number
        self.description = description

    def __eq__(self, other):
        """
        Override the natural equality check such that two Products
        are equal if they share the same serial number
        """
        return self.serial_number == other.serial_number

    def __ne__(self, other):
        """Define inequality. See __eq__."""
        return self == other

    def __hash__(self):
        """
        Override the natural hash value such that
        the hash of a product is determined by the serial number itself
        """
        return hash(self.serial_number)

    @abc.abstractmethod
    def __str__(self):
        """Enforce the abstract quality of AbstractProduct"""
        raise NotImplementedError
    
    def process(self, request, status):
        """Delegate request processing to the appropriate method"""
        if request is Exchange:
            self.processExchange(request, status)
        elif request is Refund:
            self.processRefund(request, status)
        else:
            raise ProductError(ProductType.OPOD, self.serial_number,
                               ProductError.ErrorCode.UNSUPPORTED_OPERATION)

    def processExchange(self, exchange, status):
        """Implement this in subclasses"""
        raise NotImplementedError

    def processRefund(self, refund, status):
        """Implement this in subclasses"""
        raise NotImplementedError

    @staticmethod
    def discardLesserElements(self, serial_set, min_val):
        """
        Remove from a SerialNumber set all elements below a minimum value
        """
        for candidate in serial_set:
            if candidate < min_val:
                serial_set.discard(candidate)
        return serial_set

    @staticmethod
    def discardGreaterElements(self, serial_set, max_val):
        """
        Remove from a SerialNumber set all elements above a maximum value
        """
        for candidate in serial_set:
            if candidate > max_val:
                serial_set.discard(candidate)
        return serial_set

    @staticmethod
    def computeSerialSetMean(self, serial_set):
        """Compute the average of a SerialNumber set"""
        return sum(s.serial_number for s in serial_set) / len(serial_set)

    @staticmethod
    def make(product_type, serial_number, description=None):
        """Make a Product iff all attributes are valid"""
        # cache the class associated with the product type
        product_class = eval(product_type.name.lower().capitalize())

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
        self.product_name = ProductType.OPOD.value

    def __str__(self):
        """
        Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable
        """
        out = "{name}: Serial #{serial}".format(name=self.product_name,
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out

    def processExchange(self, exchange, status):
        """Process exchanges"""

        serial_set = get_compatible_products()

        if serial_set:
            status = request_status.OK
            self.serial_number = serial_set.pop()

    def processRefund(self, refund, status):
        """Process refunds"""

        GCD_MIN = 24

        if self.serial_number.gcd(refund.rma) >= GCD_MIN:
            status = request_status.OK
            self.serial_number = None
        else:
            pass # I'd like to raise an exception, but one isn't specified

    @staticmethod
    def is_valid_serial_number(serial_number):
        """Return true iff the serial number is even
        and its third bit is not set
        """
        return serial_number.is_even() and not serial_number.test_bit(2)

class Opad(AbstractProduct):
    """Represent an oPad"""

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Opad"""
        AbstractProduct.__init__(self, serial_number, description)
        self.product_type = ProductType.OPAD
        self.product_name = ProductType.OPAD.value

    def __str__(self):
        """
        Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable
        """
        out = "{name}: Serial #{serial}".format(name=self.product_name,
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out
    
    def processExchange(self, exchange, status):
        """Process exchanges"""

        serial_set = exchange.get_compatible_products()
        best_fit_serial = SerialNumber(0)

        for candidate in serial_set:
            if  best_fit_serial < candidate < self.serial_number:
                best_fit_serial = candidate

        if best_fit_serial > SerialNumber(0):
            status = request_status.OK
            self.serial_number = best_fit_serial

    def processRefund(self, refund, status):
        """Process refunds"""

        GCD_MIN = 12

        if self.serial_number.gcd(request.rma) >= GCD_MIN:
            status = request_status.OK
            self.serial_number = None
        else:
            pass # I'd like to raise an exception, but one isn't specified

    @staticmethod
    def is_valid_serial_number(serial_number):
        """
        Return true iff the serial number is even
        and its third bit is not set
        """
        return serial_number.is_even() and serial_number.test_bit(2)

class Ophone(AbstractProduct):
    """Represent an oPhone"""

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Ophone"""
        AbstractProduct.__init__(self, serial_number, description)
        self.product_type = ProductType.OPHONE
        self.product_name = ProductType.OPHONE.value

    def __str__(self):
        """
        Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable
        """
        out = "{name}: Serial #{serial}".format(name=self.product_name,
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out
    
    def processExchange(self, exchange, status):
        """Process exchanges"""

        serial_set = Product.discardLesserElements( \
            exchange.get_compatible_products(), self.serial_number)

        average = Product.computeSerialSetMean(serial_set)
        best_fit_serial = self.serial_number

        for candidate in serial_set:
            if  best_fit_serial < candidate < average:
                best_fit_serial = candidate

        if best_fit_serial > self.serial_number:
            status = request_status.OK
            self.serial_number = best_fit_serial

    def processRefund(self, refund, status):
        """Process refunds"""
        # make three attempts at bit shifting
        for n in range(3):
            if refund.rma << n + 1 == self.serial_number:
                status = request_status.OK
                self.serial_number = None
                break
        else:
            pass # I'd like to raise an exception, but one isn't specified

    @staticmethod
    def is_valid_serial_number(serial_number):
        """
        Return true iff the serial number is odd and
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
        self.product_name = ProductType.OWATCH.value

    def __str__(self):
        """
        Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable
        """
        out = "{name}: Serial #{serial}".format(name=self.product_name,
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out
    
    def processExchange(self, exchange, status):
        """Process exchanges"""

        serial_set = exchange.get_compatible_products()
        best_fit_serial = self.serial_number

        for candidate in serial_set:
            if  self.serial_number < candidate < best_fit_serial:
                best_fit_serial = candidate

        if best_fit_serial > self.serial_number:
            status = request_status.OK
            self.serial_number = best_fit_serial

    def processRefund(self, refund, status):
        """Process refunds"""

        XOR_MIN = 14

        if self.serial_number.serial_number ^ refund.rma > XOR_MIN:
            status = request_status.OK
            self.serial_number = None
        else:
            pass # I'd like to raise an exception, but one isn't specified

    @staticmethod
    def is_valid_serial_number(serial_number):
        """
        Return true iff the serial number is odd
        and its greatest common denominator with 620 is above 14
        and less than or equal to 42
        """
        return serial_number.is_odd() and \
               14 < serial_number.gcd(SerialNumber(630)) <= 42
               
class Otv(AbstractProduct):
    """Represent an oTv"""

    def __init__(self, serial_number, description=None):
        """Initialize the attributes of this Otv"""
        AbstractProduct.__init__(self, serial_number, description)
        self.product_type = ProductType.OTV
        self.product_name = ProductType.OTV.value

    def __str__(self):
        """
        Print this Product such that the product name, serial number,
        and description (if applicable) are easily readable
        """
        out = "{name}: Serial #{serial}".format(name=self.product_name,
                                                serial=str(self.serial_number))
        if self.description != None:
            for d in self.description:
                    out += "\n" + d.capitalize()
        return out
    
    def processExchange(self, exchange, status):
        """Process exchanges"""

        UPPER_MAX = 1024

        serial_set = Product.discardLesserElements( \
            exchange.get_compatible_products(), self.serial_number)
        serial_set = Product.discardGreaterElements( \
            serial_set, self.serial_number + UPPER_MAX)
        
        average = Product.computeSerialSetMean(serial_set)
        best_fit_serial = self.serial_number

        for candidate in serial_set:
            if  best_fit_serial < candidate < average:
                best_fit_serial = candidate
        
        if best_fit_serial > self.serial_number:
            status = request_status.OK
            self.serial_number = best_fit_serial

    def processRefund(self, refund, status):
        """Process refunds"""
        if refund.rma > 0:
            status = request_status.OK
            self.serial_number = None
        else:
            pass # I'd like to raise an exception, but one isn't specified

    @staticmethod
    def is_valid_serial_number(serial_number):
        """
        Return true iff the serial number is odd and
        its greatest common denominator with 620 is less than or equal to 14
        """
        return serial_number.is_odd() and \
               serial_number.gcd(SerialNumber(630)) < 14
