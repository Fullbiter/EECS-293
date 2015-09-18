# Kevin Nash (kjn33)
# EECS 293
# Assignment 3

import unittest
from product_error import ProductError
from product_type import ProductType
from products import AbstractProduct
from products import Opod
from products import Opad
from products import Ophone
from products import Owatch
from products import Otv
from serial_number import SerialNumber

class TestPA3(unittest.TestCase):

    VALID_OPOD = SerialNumber(8)
    VALID_OPAD = SerialNumber(4)
    VALID_OPHONE = SerialNumber(45)
    VALID_OWATCH = SerialNumber(15)
    VALID_OTV = SerialNumber(1)

    def test_enum(self):
        """Test that an unknown ProductType cannot be instantiated"""
        with self.assertRaises(AttributeError):
            ProductType.INVALID
        
    def test_serial_number_gcd(self):
        """Test that gcd() returns the correct greatest common divisor."""
        self.assertEqual(SerialNumber(12).gcd(SerialNumber(34)), 2)

    def test_serial_number_mod(self):
        """Test that mod() returns the correct modulus."""
        self.assertEqual(SerialNumber(12).mod(SerialNumber(34)), 12)

    def test_serial_number_testBit(self):
        """Test that testBit() returns the correct boolean values."""
        self.assertFalse(SerialNumber(12).test_bit(0))
        self.assertTrue(SerialNumber(12).test_bit(2))

    def test_serial_number_is_even(self):
        """Test that is_even() returns the correct boolean values."""
        self.assertTrue(SerialNumber(12).is_even())
        self.assertFalse(SerialNumber(27).is_even())

    def test_serial_number_is_odd(self):
        """Test that is_odd() returns the correct boolean values."""
        self.assertFalse(SerialNumber(12).is_odd())
        self.assertTrue(SerialNumber(27).is_odd())

    def test_product_instantiation(self):
        """Test that all opod attributes are set correctly."""
        opod = AbstractProduct.make(ProductType.OPOD, self.VALID_OPOD, ["Description"])
        self.assertEqual(opod.serial_number, self.VALID_OPOD)
        self.assertEqual(opod.description, ["Description"])
        self.assertEqual(opod.product_type, ProductType.OPOD)
        self.assertEqual(opod.product_name, str(ProductType.OPOD))

    def test_product_eq(self):
        """Test that two products are equal if they share
        the same serial number, regardless of other fields.
        """
        opod_d = AbstractProduct.make(ProductType.OPOD, self.VALID_OPOD, ["Description"])
        opod_n = AbstractProduct.make(ProductType.OPOD, self.VALID_OPOD)
        self.assertEqual(opod_d, opod_n)

    def test_product_hash(self):
        """Test that two products share the same hash code if they
        share the same serial number, regardless of other fields.
        """
        opod_d = AbstractProduct.make(ProductType.OPOD, self.VALID_OPOD, ["Description"])
        opod_n = AbstractProduct.make(ProductType.OPOD, self.VALID_OPOD)
        self.assertEqual(hash(opod_d), hash(opod_n))

    def test_product_str(self):
        """Test that str() formats name, serial number,
        and descriptions correctly.
        """
        opod_d = AbstractProduct.make(ProductType.OPOD, self.VALID_OPOD, ["Description"])
        opod_n = AbstractProduct.make(ProductType.OPOD, self.VALID_OPOD)
        self.assertEqual(str(opod_n), "ProductType.OPOD: Serial #8")
        self.assertEqual(str(opod_d), "ProductType.OPOD: Serial #8\nDescription")

    def test_is_valid_serial_number(self):
        """Test that valid serial numbers return True"""
        self.assertTrue(Opod.is_valid_serial_number(self.VALID_OPOD))
        self.assertTrue(Opad.is_valid_serial_number(self.VALID_OPAD))
        self.assertTrue(Ophone.is_valid_serial_number(self.VALID_OPHONE))
        self.assertTrue(Owatch.is_valid_serial_number(self.VALID_OWATCH))
        self.assertTrue(Otv.is_valid_serial_number(self.VALID_OTV))

    def test_make_error(self):
        """Test that an erroneous SerialNumber raises an exception"""
        with self.assertRaises(ProductError):
            opod_n = AbstractProduct.make(ProductType.OPOD, SerialNumber(-1))

if __name__ == '__main__':
    unittest.main()
