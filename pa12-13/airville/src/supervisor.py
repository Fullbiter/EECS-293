# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from actor import Actor
from random import choice
from random import randint

class Supervisor(Actor):
    """ Supervisor personnel assist Agents """

    def __init__(self, counters, machines):
        super(Supervisor, self).__init__()
        self.counters = counters
        self.machines = machines

    def act(self):
        """
        Find a station,
        or wander,
        or report supervising

        return status as string
        """
        if self.location is None:
            return self.find_station()
        elif randint(1, 4) % 4 == 0:
            return self.wander()
        else:
            return "is supervising %s" % self.location

    def find_station(self):
        """
        Find an unmanned station, join station if one is found

        return status as string
        """
        try:
            self.location = next(c for c in self.counters
                                 if c.supervisor is None)
        except StopIteration:
            try:
                self.location = next(m for m in self.machines
                                     if m.supervisor is None)
            except StopIteration:
                return "found no open stations and stayed put"
        self.location.supervise_station(self)
        return "joined %s" % str(self.location)

    def wander(self):
        """
        Randomly move between stations

        return status as string
        """
        available_stations = self.counters + self.machines
        available_stations.remove(self.location)
        self.location = choice(available_stations)
        return "wandered to %s" % str(self.location)
