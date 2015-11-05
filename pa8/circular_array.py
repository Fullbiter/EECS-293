# Kevin Nash (kjn33)
# EECS 293
# Assignment 8


class CircularArray:
    """
    A circular array implementation of the running maximum data structure
    """

    def __init__(self, k):
        """ Initialize the array of size k and head index """
        if not isinstance(k, int):
            raise TypeError("argument is not an integer")
        if k < 1:
            raise Exception("integer argument is non-positive")
        self.a = [None] * k
        self.head = 0

    def offer(self, x):
        """ Add x to the current head index """
        self.a[self.head % len(self.a)] = x
        self.head += 1

    def maximum(self):
        """
        Return the maximum value of the array,
        or None if the array is empty        
        """
        if self.head > 0:
            return max(self.a[0:min(self.head, len(self.a))])
        return None
