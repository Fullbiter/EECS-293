# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from entity import Entity


class Machine(Entity):
    """ An Entity that can be used by PassengerGroups """

    def __init__(self):
        """
        Machines follow Entity initialization,
        are given a null PassengerGroup and Supervisor
        """
        super(Machine, self).__init__()
        self.group = None
        self.supervisor = None

    def use(self, group):
        """ Set the local PassengerGroup to the provided PassengerGroup """
        self.group = group

    def finish(self):
        """ Set the local PassengerGroup to None """
        self.group = None

    def supervise_station(self, supervisor):
        """ Set the local Supervisor to the provided Supervisor """
        self.supervisor = supervisor
