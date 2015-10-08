# Kevin Nash (kjn33)
# EECS 293
# Assignment 6

import time

class CircularArray:
    """ """

    def __init__(self, k):
        """ """
        self.a = [None for _ in xrange(k)]
        self.head = 0

    def offer(self, x):
        """ """
        self.a[self.head % len(self.a)] = x
        self.head += 1

    def maximum(self):
        """ """
        if self.head > 0:
            return max(self.a[0:min(self.head, len(self.a))])
        return None
