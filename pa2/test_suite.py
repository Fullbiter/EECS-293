# Kevin Nash (kjn33)
# EECS 293
# Assignment 2

import unittest
from abstract_product import AbstractProduct
from opod import Opod
from product_type import ProductType
from serial_number import SerialNumber

class TestPA2(unittest.TestCase):

    def definition():
        self.product_opod = ProductType.OPOD
        self.serial_12 = SerialNumber(12)
        self.serial_27 = SerialNumber(27)
        self.serial_34 = SerialNumber(34)
        self.opod_n = Opod(serial_12)
        self.description = ["plays music", "wifi enabled"]
        self.opod_d = Opod(serial_12, description)

    def test_product_type_instatiation(self):
        """Test that a proper ProductType can be instantiated
        and that an unknown type cannot.
        """
        self.assertRaises(AttributeError, ProductType.FOO)

    def test_product_type_str(self):
        """Test that ProductType can return
        its name in the correct format.
        """
        self.assertEqual(product_type.__str__(), 'oPod')
        
    def test_serial_number_instantiation(self):
        """Test that instantiating a SerialNumber
        will give it the expected value.
        """
        self.assertEqual(serial_12.serial_number, 12)

    def test_serial_number_gcd(self):
        """Test that gcd() returns the correct greatest common divisor."""
        self.assertEqual(serial_12.gcd(serial_34), 2)

    def test_serial_number_mod(self):
        """Test that mod() returns the correct modulus."""
        self.assertEqual(serial_12.mod(serial_34), 12)

    def test_serial_number_testBit(self):
        """Test that testBit() returns the correct boolean values."""
        self.assertFalse(serial_12.test_bit(0))
        self.assertTrue(serial_12.test_bit(2))

    def test_serial_number_is_even(self):
        """Test that is_even() returns the correct boolean values."""
        self.assertTrue(serial_12.is_even())
        self.assertFalse(serial_27.is_even())

    def test_serial_number_is_odd(self):
        """Test that is_odd() returns the correct boolean values."""
        self.assertFalse(serial_12.is_odd())
        self.assertTrue(serial_27.is_odd())

    def test_abstract_product_str(self):
        """Test that __str__(), as an abstract method,
        raises a NotImplementedError.
        """
        abstract_product = AbstractProduct(serial_12)
        self.assertRaises(NotImplementedError, abstract_product.__str__())

    def test_opod_instantiation(self):
        """Test that all opod attributes are set correctly."""
        self.assertEqual(opod_n.serial_number, serial_12)
        self.assertEqual(opod_n.description, description)
        self.assertEqual(opod_n.product_type, ProductType.OPOD)
        self.assertEqual(opod_n.product_name, ProductType.OPOD.__str__())

    def test_opod_eq(self):
        """Test that two Opods are equal if they share
        the same serial number, regardless of other fields.
        """
        self.assertEqual(opod_n, opod_d)

    def test_opod_hash(self):
        """Test that two Opods share the same hash code if they
        share the same serial number, regardless of other fields.
        """
        self.assertEqual(hash(opod_n), hash(opod_d))

    def test_opod_str(self):
        """Test that __str__() formats name, serial number,
        and descriptions correctly.
        """
        self.assertEqual(opod_n.__str__(),
                         "oPod: Serial #12")
        self.assertEqual(opod_d.__str__(),
                         "oPod: Serial #12\nPlays music\nWifi enabled")

    def test_opod_is_valid_serial_number(self):
        """Test that serial numbers are only checked valid
        if they are even and their third bit is not set.
        """
        self.assertFalse(Opod.is_valid_serial_number(serial_12))
        self.assertFalse(Opod.is_valid_serial_number(serial_27))
        self.assertTrue(Opod.is_valid_serial_number(serial_34))

if __name__ == '__main__':
    unittest.main()
