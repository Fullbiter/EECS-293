# Kevin Nash (kjn33)
# EECS 293
# Assignment 7

import time
import unittest

from circular_array import CircularArray


class TestCircularArray(unittest.TestCase):
    """ Run tests regarding CircularArray """

    def test_empty(self):
        """ Test a call to maximum() on an empty array """
        a = CircularArray(3)
        self.assertEqual(a.a, [None, None, None])
        self.assertEqual(a.maximum(), None)

    def test_full(self):
        """ Test a call to maximum() """
        a = CircularArray(3)
        for x in xrange(1, 4):
            a.offer(x)
        self.assertEqual(a.a, [1, 2, 3])
        self.assertEqual(a.maximum(), 3)

    def test_wrapped(self):
        """ Test the circular property of the array """
        a = CircularArray(3)
        for x in xrange(1, 7):
            a.offer(x)
        self.assertEqual(a.a, [4, 5, 6])
        self.assertEqual(a.maximum(), 6)

    def test_k_not_met(self):
        """ Test that maximum() compares only necessary indices """
        a = CircularArray(100000000) # one hundred million
        a.offer(1)
        start = time.clock()
        a.maximum()
        end = time.clock()
        self.assertTrue(end - start < 1e-04)

if __name__ == '__main__':
    unittest.main()
