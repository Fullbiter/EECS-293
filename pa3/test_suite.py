# Kevin Nash (kjn33)
# EECS 293
# Assignment 3

import unittest
from product_type import ProductType
import products
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

    def test_opod_instantiation(self):
        """Test that all opod attributes are set correctly."""
        self.assertEqual(self.opod_n.serial_number, SerialNumber(12))
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
        self.assertFalse(Opod.is_valid_serial_number(SerialNumber(12)))
        self.assertFalse(Opod.is_valid_serial_number(SerialNumber(27)))
        self.assertTrue(Opod.is_valid_serial_number(SerialNumber(34)))

if __name__ == '__main__':
    unittest.main()
