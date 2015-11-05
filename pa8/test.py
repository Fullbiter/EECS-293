# Kevin Nash (kjn33)
# EECS 293
# Assignment 8

import unittest

from circular_array import CircularArray

from random import randint


class TestCircularArray(unittest.TestCase):
    """ Run tests regarding CircularArray """

    def test_init_non_integer(self):
        """
        Test initialization given a non-integer value
            Structured basis:   first condition is true
            Bad data:           k is not an integer
        """
        with self.assertRaises(TypeError):
            a = CircularArray("string")

    def test_init_non_positive(self):
        """
        Test initialization given a non-positive integer value
            Structured basis:   second condition is true
            Bad data:           k is a non-positive integer
        """
        with self.assertRaises(Exception):
            a = CircularArray(-1)

    def test_init_nominal(self):
        """
        Test initialization given a positive integer value
            Structured basis:   nominal case
            Data flow:          a Defined, head Defined
            Good data:          k is a positive integer
        """
        a = CircularArray(1)
        self.assertEqual(len(a.a), 1)
        self.assertEqual(a.head, 0)

    def test_offer_head_left(self):
        """
        Test offer to a CircularArray when head is less than the length of a
            Data flow:  a Used, head Used
            Boundary:   head < len(a)
        """
        a = CircularArray(3)
        self.assertEqual(a.a, [None, None, None])
        self.assertEqual(a.head, 0)
        a.offer(0)
        self.assertEqual(a.a, [0, None, None])
        self.assertEqual(a.head, 1)

    def test_offer_head_right(self):
        """
        Test offer to a CircularArray when head is equal to the length of a
            Data flow:  a Used, head Used
            Boundary:   head >= len(a)
        """
        a = CircularArray(3)
        a.offer(0)
        a.offer(1)
        a.offer(2)
        self.assertEqual(a.a, [0, 1, 2])
        self.assertEqual(a.head, 3)
        a.offer(3)
        self.assertEqual(a.a, [3, 1, 2])
        self.assertEqual(a.head, 4)

    def test_maximum_left(self):
        """
        Test calling maximum on an empty array
            Structured basis:   initial condition not met
            Boundary:           head <= 0
        """
        a = CircularArray(3)
        self.assertEqual(a.a, [None, None, None])
        self.assertEqual(a.maximum(), None)

    def test_maximum_middle(self):
        """
        Test calling maximum on a partially filled array
            Structured basis:   initial condition met
            Boundary:           len(a) > head > 0
        """
        a = CircularArray(3)
        a.offer(1)
        self.assertEqual(a.maximum(), 1)
        a.offer(3)
        self.assertEqual(a.maximum(), 3)
        a.offer(2)
        self.assertEqual(a.maximum(), 3)
        self.assertEqual(a.a, [1, 3, 2])

    def test_maximum_right(self):
        """
        Test calling maximum on an overfilled array
            Structured basis:   initial condition met
            Boundary:           head >= len(a) > 0
        """
        # pre-wrap
        a = CircularArray(3)
        a.offer(1)
        self.assertEqual(a.maximum(), 1)
        a.offer(3)
        self.assertEqual(a.maximum(), 3)
        a.offer(2)
        self.assertEqual(a.maximum(), 3)
        self.assertEqual(a.a, [1, 3, 2])

        # post-wrap
        a.offer(0)
        self.assertEqual(a.maximum(), 3)
        a.offer(0)
        self.assertEqual(a.maximum(), 2)
        self.assertEqual(a.a, [0, 0, 2])

    def test_stress(self):
        """
        Stress test entire class
        Warning: this test has a long runtime
        """
        
        BIG_NUMBER = 1000000  # one million
        a = CircularArray(BIG_NUMBER)
        
        # populate first half with random integers
        for _ in xrange(BIG_NUMBER / 2):
            a.offer(randint(0, 9))
        
        # offer the maximum
        a.offer(10)

        # populate second half with random integers
        for _ in xrange(BIG_NUMBER / 2, BIG_NUMBER):
            a.offer(randint(0, 9))

        self.assertEqual(a.maximum(), 10)

    def test_k_not_met(self):
        """ Test that maximum only considers elements within head """
        a = CircularArray(3)
        a.offer(5)
        a.a[1] = 10  # direct assignment
        self.assertEqual(a.a, [5, 10, None])
        self.assertEqual(a.maximum(), 5)


if __name__ == '__main__':
    unittest.main()
