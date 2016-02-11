# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from entity import Entity


class Counter(Entity):
    """ A Location at which Agents and Supervisors can work """

    def __init__(self):
        """
        Counters follow Entity initialization,
        are given null Agent and Supervisor values
        """
        super(Counter, self).__init__()
        self.agent = None
        self.supervisor = None

    def man_station(self, agent):
        """ Set the Counter's Agent to the provided object """
        self.agent = agent

    def supervise_station(self, supervisor):
        """ Set the Counter's Supervisor to the provided object"""
        self.supervisor = supervisor

