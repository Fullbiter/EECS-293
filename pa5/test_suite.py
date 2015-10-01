# Kevin Nash (kjn33)
# EECS 293
# Assignment 4

import unittest

from product_error import ProductError

from product_type import ProductType

from products import AbstractProduct
from products import Opod
from products import Opad
from products import Ophone
from products import Owatch
from products import Otv

from requests import Exchange
from requests import Refund
from requests import Request

from request_error import RequestError

from request_status import RequestStatus

from serial_number import SerialNumber

class TestProductType(unittest.TestCase):
    """Run tests regarding ProductType."""

    def test_get_name(self):
        """Test the ability to retrieve the product name."""
        self.assertEqual(ProductType.OPOD.value, "oPod")
        self.assertEqual(ProductType.OPAD.value, "oPad")
        self.assertEqual(ProductType.OPHONE.value, "oPhone")
        self.assertEqual(ProductType.OWATCH.value, "oWatch")
        self.assertEqual(ProductType.OTV.value, "oTv")

    def test_enum(self):
        """Test that only valid ProductTypes can be referenced."""
        with self.assertRaises(AttributeError):
            ProductType.INVALID

class TestSerialNumber(unittest.TestCase):
    """Run tests regarding SerialNumber."""

    def test_get_serial_number(self):
        """Test the ability to retrieve the serial number."""
        s = SerialNumber(12)
        self.assertEqual(s.serial_number, 12)
        
    def test_gcd(self):
        """Test that the greatest common divisor is found correctly."""
        s1 = SerialNumber(12)
        s2 = SerialNumber(34)
        self.assertEqual(s1.gcd(s2), 2)

    def test_mod(self):
        """Test that the modulus is found correctly."""
        s1 = SerialNumber(12)
        s2 = SerialNumber(34)
        self.assertEqual(s1.mod(s2), 12)

    def test_test_bit(self):
        """Test that the truth value of a bit is found correctly."""
        s = SerialNumber(12)
        self.assertFalse(s.test_bit(0))
        self.assertTrue(s.test_bit(2))

    def test_is_even(self):
        """Test that even serial numbers are identified."""
        s1 = SerialNumber(12)
        s2 = SerialNumber(27)
        self.assertFalse(s2.is_even())
        self.assertTrue(s1.is_even())

    def test_is_odd(self):
        """Test that odd serial numbers are identified."""
        s1 = SerialNumber(12)
        s2 = SerialNumber(27)
        self.assertFalse(s1.is_odd())
        self.assertTrue(s2.is_odd())

    def test_ordering(self):
        """Test that serial numbers are ordered by their numbers."""
        s1 = SerialNumber(12)
        s2 = SerialNumber(27)
        s3 = SerialNumber(34)
        s_all = [s3, s1, s2]    # note the order
        self.assertEqual(sorted(s_all), [s1, s2, s3])

class TestProductError(unittest.TestCase):
    """Run tests regarding ProductError."""

    pt = ProductType.OPOD
    sn = SerialNumber(12)
    ec = ProductError.ErrorCode(1)
    err = ProductError(pt, sn, ec)

    def test_get_product_type(self):
        """Test the ability to retrieve the product type."""
        self.assertEqual(self.err.product_type, self.pt)

    def test_get_product_name(self):
        """Test the ability to retrieve the product name."""
        self.assertEqual(self.err.product_name, self.pt.value)

    def test_get_serial_number(self):
        """Test the ability to retrieve the serial number."""
        self.assertEqual(self.err.serial_number, self.sn)

    def test_get_error_code(self):
        """Test the ability to retrieve the error code."""
        self.assertEqual(self.err.error_code, self.ec)

class TestProducts(unittest.TestCase):
    """Run tests regarding all Products."""

    # Valid serial numbers for each product
    VALID_OPOD = SerialNumber(8)
    VALID_OPAD = SerialNumber(4)
    VALID_OPHONE = SerialNumber(45)
    VALID_OWATCH = SerialNumber(15)
    VALID_OTV = SerialNumber(1)

    desc = ["Description A", "Description B"]

    # Product objects with descriptions
    opod_d = Opod(VALID_OPOD, desc)
    opad_d = Opad(VALID_OPAD, desc)
    ophone_d = Ophone(VALID_OPHONE, desc)
    owatch_d = Owatch(VALID_OWATCH, desc)
    otv_d = Otv(VALID_OTV, desc)

    # Product objects with no description
    opod_n = Opod(VALID_OPOD)
    opad_n = Opad(VALID_OPAD)
    ophone_n = Ophone(VALID_OPHONE)
    owatch_n = Owatch(VALID_OWATCH)
    otv_n = Otv(VALID_OTV)

    def test_get_serial_number(self):
        """Test the ability to retrieve the serial number."""
        self.assertEqual(self.opod_n.serial_number, self.VALID_OPOD)
        self.assertEqual(self.opad_n.serial_number, self.VALID_OPAD)
        self.assertEqual(self.ophone_n.serial_number, self.VALID_OPHONE)
        self.assertEqual(self.owatch_n.serial_number, self.VALID_OWATCH)
        self.assertEqual(self.otv_n.serial_number, self.VALID_OTV)

    def test_get_product_type(self):
        """Test the ability to retrieve the product type."""
        self.assertEqual(self.opod_n.product_type, ProductType.OPOD)
        self.assertEqual(self.opad_n.product_type, ProductType.OPAD)
        self.assertEqual(self.ophone_n.product_type, ProductType.OPHONE)
        self.assertEqual(self.owatch_n.product_type, ProductType.OWATCH)
        self.assertEqual(self.otv_n.product_type, ProductType.OTV)

    def test_get_product_name(self):
        """Test the ability to retrieve the product name."""
        self.assertEqual(self.opod_n.product_name, ProductType.OPOD.value)
        self.assertEqual(self.opad_n.product_name, ProductType.OPAD.value)
        self.assertEqual(self.ophone_n.product_name, ProductType.OPHONE.value)
        self.assertEqual(self.owatch_n.product_name, ProductType.OWATCH.value)
        self.assertEqual(self.otv_n.product_name, ProductType.OTV.value)

    def test_get_description(self):
        """Test the ability to retrieve the product description."""
        self.assertEqual(self.opod_d.description, self.desc)
        self.assertEqual(self.opad_d.description, self.desc)
        self.assertEqual(self.ophone_d.description, self.desc)
        self.assertEqual(self.owatch_d.description, self.desc)
        self.assertEqual(self.otv_d.description, self.desc)

    def test_is_valid_serial_number(self):
        """Test that valid serial numbers are identified."""
        self.assertTrue(Opod.is_valid_serial_number(self.VALID_OPOD))
        self.assertTrue(Opad.is_valid_serial_number(self.VALID_OPAD))
        self.assertTrue(Ophone.is_valid_serial_number(self.VALID_OPHONE))
        self.assertTrue(Owatch.is_valid_serial_number(self.VALID_OWATCH))
        self.assertTrue(Otv.is_valid_serial_number(self.VALID_OTV))

    def test_equality(self):
        """
        Test that two products are equal if they share
        the same serial number, regardless of other fields.
        """
        self.assertEqual(self.opod_d, self.opod_n)
        self.assertEqual(self.opad_d, self.opad_n)
        self.assertEqual(self.ophone_d, self.ophone_n)
        self.assertEqual(self.owatch_d, self.owatch_n)
        self.assertEqual(self.otv_d, self.otv_n)

    def test_hash(self):
        """
        Test that two products share the same has code if they
        share the same serial number, regardless of other fields.
        """
        self.assertEqual(hash(self.opod_d), hash(self.opod_n))
        self.assertEqual(hash(self.opad_d), hash(self.opad_n))
        self.assertEqual(hash(self.ophone_d), hash(self.ophone_n))
        self.assertEqual(hash(self.owatch_d), hash(self.owatch_n))
        self.assertEqual(hash(self.otv_d), hash(self.otv_n))

class TestAbstractProduct(unittest.TestCase):
    """Run tests regarding AbstractProduct."""

    # Valid serial numbers for each product
    VALID_OPOD = SerialNumber(8)
    VALID_OPAD = SerialNumber(4)
    VALID_OPHONE = SerialNumber(45)
    VALID_OWATCH = SerialNumber(15)
    VALID_OTV = SerialNumber(1)

    # Products instantiated directly
    opod = Opod(VALID_OPOD)
    opad = Opad(VALID_OPAD)
    ophone = Ophone(VALID_OPHONE)
    owatch = Owatch(VALID_OWATCH)
    otv = Otv(VALID_OTV)

    def test_make(self):
        """Test that the factory method correctly makes a product."""
        
        # Products instantiated by the factory method
        opod_f = AbstractProduct.make(ProductType.OPOD, self.VALID_OPOD)
        opad_f = AbstractProduct.make(ProductType.OPAD, self.VALID_OPAD)
        ophone_f = AbstractProduct.make(ProductType.OPHONE, self.VALID_OPHONE)
        owatch_f = AbstractProduct.make(ProductType.OWATCH, self.VALID_OWATCH)
        otv_f = AbstractProduct.make(ProductType.OTV, self.VALID_OTV)

        self.assertEqual(self.opod, opod_f)
        self.assertEqual(self.opad, opad_f)
        self.assertEqual(self.ophone, ophone_f)
        self.assertEqual(self.owatch, owatch_f)
        self.assertEqual(self.otv, otv_f)

    def test_make_error(self):
        """
        Test that a product cannot be made with
        an invalid serial number or product type.
        """
        with self.assertRaises(ProductError):
            AbstractProduct.make(ProductType.OPOD, SerialNumber(0))
        with self.assertRaises(ProductError):
            AbstractProduct.make(ProductType.OPAD, SerialNumber(0))
        with self.assertRaises(ProductError):
            AbstractProduct.make(ProductType.OPHONE, SerialNumber(0))
        with self.assertRaises(ProductError):
            AbstractProduct.make(ProductType.OWATCH, SerialNumber(0))
        with self.assertRaises(ProductError):
            AbstractProduct.make(ProductType.OTV, SerialNumber(0))
        
        with self.assertRaises(AttributeError):
            AbstractProduct.make(ProductType.INVALID, SerialNumber(0))

    def test_abstract(self):
        """Test that AbstractProduct cannot be instantiated"""
        with self.assertRaises(TypeError):
            ap = AbstractProduct(0)

class TestRequest(unittest.TestCase):
    """Run tests regarding Request"""

    def test_abstract(self):
        """Test that Request cannot be instantiated"""
        with self.assertRaises(TypeError):
            r = Request()

class TestExchange(unittest.TestCase):
    """Run tests regarding Exchange"""

    s1 = SerialNumber(1)
    s2 = SerialNumber(2)
    s3 = SerialNumber(3)
    s4 = SerialNumber(4)

    def test_immutability(self):
        """Test that an Exchange is not affected by changes to its builder"""
        # Build with serial numbers 1 and 2
        builder = Exchange.Builder()
        builder.add_compatible(self.s1).add_compatible(self.s2)
        exchange = builder.build()
        # Add serial number 3 without building
        builder.add_compatible(self.s3)

        self.assertEqual(exchange.compatible_products, {self.s1, self.s2})

        products = exchange.get_compatible_products()
        products.add(self.s4)

        self.assertEqual(exchange.compatible_products, {self.s1, self.s2})

    def test_opad_exchange(self):
        """Test that opad exchanges are handled correctly"""
        opad1048 = Opad(SerialNumber(1048))
        opad1244 = Opad(SerialNumber(1244))
        status = RequestStatus()
        builder = Exchange.Builder()
        builder.add_compatible(opad1244.serial_number)
        exchange = builder.build()

        exchange.process(opad1048, status)

        self.assertEqual(status.status_code, RequestStatus.StatusCode.OK)

class TestRefund(unittest.TestCase):
    """Run tests regarding Refund"""

    def test_invalid_rma(self):
        """Test that invalid RMA codes are not processed"""
        builder = Refund.Builder()
        with self.assertRaises(RequestError):
            builder.set_rma(None)

    def test_rma(self):
        """"""
        builder = Refund.Builder()
        builder.set_rma(9999999999)

if __name__ == '__main__':
    unittest.main()
