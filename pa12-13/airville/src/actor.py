# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from entity import Entity


class Actor(Entity):
    """ A game entity that can act and be acted upon """

    def __init__(self):
        """
        Actors follow Entity initialization,
        are given a null location
        """
        super(Actor, self).__init__()
        self.location = None

    def act(self):
        """
        return status as string,
        overridden by subclasses
        """
        return "did nothing"
