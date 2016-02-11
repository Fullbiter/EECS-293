# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from actor import Actor
from machine import Machine
from operator import attrgetter


class PassengerGroup(Actor):
    """ """

    def __init__(self, passengers, lines_regular,
                 lines_frequent, lines_automated, machines):
        """
        Lines follow Entity initialization,
        are given "sight" of relevant Locations
        """
        super(PassengerGroup, self).__init__()
        self.passengers = passengers
        # is everyone in the group a frequent flyer
        self.frequent = all(p.frequent for p in passengers)
        self.lines_regular = lines_regular
        self.lines_frequent = lines_frequent
        self.lines_automated = lines_automated
        self.machines = machines

    def act(self):
        """
        Queue at a Line,
        or use a check in machine,
        or walk to a check in machine
        """
        if self.location is None:
            return self.queue()
        if type(self.location) is Machine:
            return self.use_machine()
        if self.location.automated and self.location.get_first() is self:
            return self.go_to_machine()

    def queue(self):
        """
        Line up at the shortest line that matches frequent flyer status

        return status as string
        """
        if self.frequent and len(self.lines_frequent) > 0:
            self.location = min(self.lines_frequent, key=attrgetter('length'))
        else:
            lines_available = self.lines_regular + self.lines_automated
            self.location = min(lines_available, key=attrgetter('length'))
        self.location.enter(self)
        return "joined %s" % str(self.location)

    def go_to_machine(self):
        """
        Try to find an open machine, use that machine if successful,
        otherwise report waiting

        return status as string
        """
        machine = self.find_open_machine()
        if machine is None:
            return "is first in line waiting for an open machine"
        machine.use(self.location.exit())
        self.location = machine
        return "moved to %s" % self.location

    def find_open_machine(self):
        """
        Find a machine that does not have an associated PassengerGroup

        return the first open machine
        """
        try:
            return next(m for m in self.machines if m.group is None)
        except StopIteration:
            return None

    def use_machine(self):
        """
        Check in Passengers within the PassengerGroup one turn at a time,
        or report the end of check in

        return status as string
        """
        try:
            passenger = self.pop()
            return "checked in %s at %s" % (passenger, self.location)
        except IndexError:
            self.location.finish()
            machine = self.location
            self.location = None
            return "finished using %s" % machine

    def pop(self):
        """ Pop the next passenger in this PassengerGroup """
        return self.passengers.pop()

    def __str__(self):
        """ Represent PassengerGroup by name, ID, and flyer type """
        flyer_type = "regular"
        if self.frequent:
            flyer_type = "frequent"
        return "%s %d (%s)" % (self.__class__.__name__, self.id, flyer_type)
