# Kevin Nash (kjn33)
# EECS 293
# Assignment 12


class Entity(object):
    """ A game entity that can be acted upon """

    lastID = 0

    def __init__(self):
        """ Update the ID number of the calling class and instance """
        self.__class__.lastID += 1
        self.id = self.__class__.lastID

    def __str__(self):
        """ Represent entity by name and ID """
        return "%s %d" % (self.__class__.__name__, self.id)
