# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from entity import Entity
from random import randint


class Passenger(Entity):
    """ Entities that need to be checked in following queueing """

    def __init__(self):
        """
        Passengers follow Entity initialization,
        are randomly given special parameters
        """

        super(Passenger, self).__init__()
        
        # 50% chance of being a frequent flyer
        self.frequent = randint(1, 2) % 2 == 0
        # 10% chance of having a given special condition
        self.oversize = randint(1, 10) % 10 == 0
        self.rerouted = randint(1, 10) % 10 == 0
        self.overbook = randint(1, 10) % 10 == 0

        self.time = 2
        self.calc_time()

    def __str__(self):
        """ Represent Passenger by name, ID, and flyer type """
        flyer_type = "regular"
        if self.frequent:
            flyer_type = "frequent"
        return "%s %d (%s)" % (self.__class__.__name__, self.id, flyer_type)

    def calc_time(self):
        """ Set the time required for check in based on special parameters """
        if self.oversize:
            self.time += 2
        if self.rerouted:
            self.time += 2
        if self.overbook:
            self.time += 2
