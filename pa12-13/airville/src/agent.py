# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from operator import attrgetter

from actor import Actor
from counter import Counter
from passenger_group import PassengerGroup


class Agent(Actor):
    """ Actor that checks in Passengers """

    def __init__(self, counters, machines, lines_regular, lines_frequent):
        """
        Agents follow Entity initialization,
        are given "sight" of relevant Locations
        """
        super(Agent, self).__init__()
        self.counters = counters
        self.machines = machines
        self.lines_regular = lines_regular
        self.lines_frequent = lines_frequent
        self.group = None

    def act(self):
        """
        Find a station to work at,
        or check in a group,
        or call over the next group

        return status as string
        """
        if self.group is not None:
            return self.check_in()
        elif self.location is None:
            return self.find_station()
        elif type(self.location) is Counter:
            return self.call_from_line()

    def find_station(self):
        """
        Find an unmanned station, join station if one is found 

        return status as string
        """
        try:
            self.location = next(c for c in self.counters if c.agent is None)
        except StopIteration:
            return "found no open stations and stayed put"
        self.location.man_station(self)
        return "joined %s" % str(self.location)

    def call_from_line(self):
        """
        Call a PassengerGroup over from the most appropriate Line,
        Priority is by frequent flyer / normal and then by descending length

        return status as string
        """
        if len(self.lines_frequent) > 0:
            line = max(self.lines_frequent, key=attrgetter('length'))
            if line.length > 0:
                self.group = line.exit()
                return "called over %s" % self.group
        
        if len(self.lines_regular) > 0:
            line = max(self.lines_regular, key=attrgetter('length'))
            if line.length > 0:
                self.group = line.exit()
                return "called over %s" % self.group

        return "reported that all lines are empty"

    def check_in(self):
        """
        Check in the PassengerGroup at hand, or report the end of processing

        return status as string
        """
        try:
            passenger = self.group.pop()
            time = passenger.time
            if self.location.supervisor is not None:
                time /= 2
            return "checked in %s in %d minutes" % (passenger, time)
        except IndexError:
            s = str(self.group)
            self.group = None
            return "finished processing %s" % s
