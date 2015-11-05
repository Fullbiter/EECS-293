# Kevin Nash (kjn33)
# EECS 293
# Assignment 10

import blacklist
import unittest

class TestBlacklist(unittest.TestCase):
    """ Run tests regarding blacklist.py """

    def test_combine_dicts(self):
        """ Test nominal case """
        a = {"a": 1, "b": 1}
        b = {"b": 1, "c": 3}
        c = blacklist._combine_dicts(a, b)
        self.assertEqual(c, {"a": 1, "b": 2, "c": 3})        

if __name__ == '__main__':
    unittest.main()
