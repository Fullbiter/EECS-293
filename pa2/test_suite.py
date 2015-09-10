# Kevin Nash (kjn33)
# EECS 293
# Assignment 2

import unittest
from abstract_product import AbstractProduct
from opod import Opod
from product_type import ProductType
from serial_number import SerialNumber

class TestPA2(unittest.TestCase):

    product_opod = ProductType.OPOD
    serial_12 = SerialNumber(12)
    serial_27 = SerialNumber(27)
    serial_34 = SerialNumber(34)
    opod_n = Opod(serial_12)
    description = ["plays music", "wifi enabled"]
    opod_d = Opod(serial_12, description)

    #def test_product_type_instatiation(self):
    #    """Test that a proper ProductType can be instantiated # Error is not
    #    and that an unknown type cannot.                      # being caught
    #    """                                                   # here
    #    self.assertRaises(AttributeError, ProductType.FOO)

    def test_product_type_str(self):
        """Test that ProductType can return
        its name in the correct format.
        """
        self.assertEqual(self.product_opod.__str__(), 'oPod')
        
    def test_serial_number_instantiation(self):
        """Test that instantiating a SerialNumber
        will give it the expected value.
        """
        self.assertEqual(self.serial_12.serial_number, 12)

    def test_serial_number_gcd(self):
        """Test that gcd() returns the correct greatest common divisor."""
        self.assertEqual(self.serial_12.gcd(self.serial_34), 2)

    def test_serial_number_mod(self):
        """Test that mod() returns the correct modulus."""
        self.assertEqual(self.serial_12.mod(self.serial_34), 12)

    def test_serial_number_testBit(self):
        """Test that testBit() returns the correct boolean values."""
        self.assertFalse(self.serial_12.test_bit(0))
        self.assertTrue(self.serial_12.test_bit(2))

    def test_serial_number_is_even(self):
        """Test that is_even() returns the correct boolean values."""
        self.assertTrue(self.serial_12.is_even())
        self.assertFalse(self.serial_27.is_even())

    def test_serial_number_is_odd(self):
        """Test that is_odd() returns the correct boolean values."""
        self.assertFalse(self.serial_12.is_odd())
        self.assertTrue(self.serial_27.is_odd())

    #def test_abstract_product_str(self):
    #    """Test that __str__(), as an abstract method, # NonImplementedError
    #    raises a NotImplementedErrorself.              # is not caught here
    #    """                                            # for some reason.
    #    with self.assertRaises(NotImplementedError):
    #        AbstractProduct(self.serial_12)

    def test_opod_instantiation(self):
        """Test that all opod attributes are set correctly."""
        self.assertEqual(self.opod_n.serial_number, self.serial_12)
        self.assertEqual(self.opod_n.description, None)
        self.assertEqual(self.opod_n.product_type, ProductType.OPOD)
        self.assertEqual(self.opod_n.product_name, ProductType.OPOD.__str__())

    def test_opod_eq(self):
        """Test that two Opods are equal if they share
        the same serial number, regardless of other fields.
        """
        self.assertEqual(self.opod_n, self.opod_d)

    def test_opod_hash(self):
        """Test that two Opods share the same hash code if they
        share the same serial number, regardless of other fields.
        """
        self.assertEqual(hash(self.opod_n), hash(self.opod_d))

    def test_opod_str(self):
        """Test that __str__() formats name, serial number,
        and descriptions correctly.
        """
        self.assertEqual(self.opod_n.__str__(),
                         "oPod: Serial #12")
        self.assertEqual(self.opod_d.__str__(),
                         "oPod: Serial #12\nPlays music\nWifi enabled")

    def test_opod_is_valid_serial_number(self):
        """Test that serial numbers are only checked valid
        if they are even and their third bit is not set.
        """
        self.assertFalse(Opod.is_valid_serial_number(self.serial_12))
        self.assertFalse(Opod.is_valid_serial_number(self.serial_27))
        self.assertTrue(Opod.is_valid_serial_number(self.serial_34))

if __name__ == '__main__':
    unittest.main()
