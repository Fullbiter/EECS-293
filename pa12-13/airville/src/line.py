# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from entity import Entity


class Line(Entity):
    """ A Location where Passengers can line up """

    def __init__(self, frequent=False, automated=False):
        """
        Lines follow Entity initialization,
        can be given special parameters
        """
        super(Line, self).__init__()
        self.frequent = frequent
        self.automated = automated
        self.groups = []
        self.length = len(self.groups)

    def enter(self, group):
        """ Insert a new PassengerGroup at the end of the line """
        self.groups.insert(0, group)
        self.length = len(self.groups)

    def exit(self):
        """
        Unless the line is empty, pop the group at the front of the line
        """
        if self.length > 0:
            self.length = len(self.groups) - 1
            return self.groups.pop()

    def get_first(self):
        """ Return the first group in the Line """
        return self.groups[-1]

    def __str__(self):
        """ Represent Line with ID, type, and length """
        line_type = "regular"
        if self.frequent:
            line_type = "frequent"
        elif self.automated:
            line_type = "automated"
        return "Line %d (%s, %d waiting)" % (self.id, line_type, self.length)
