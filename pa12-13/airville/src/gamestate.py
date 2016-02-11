# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from operator import attrgetter
from random import choice
from random import getrandbits
from time import sleep

from agent import Agent
from supervisor import Supervisor
from passenger import Passenger
from passenger_group import PassengerGroup

from counter import Counter
from machine import Machine
from line import Line


class GSM:
    """ GameStateManager that manages all high level game functions """

    agents = []
    supervisors = []
    groups = []

    counters = []
    machines = []
    lines_regular = []
    lines_frequent = []
    lines_automated = []

    def __init__(self):
        """ Set option parameters to magic values """

        # inital actors
        self.NUM_AGENTS = 2
        self.NUM_SUPERVISORS = 1
        self.NUM_GROUPS = 3

        # initial locations
        self.NUM_COUNTERS = 2
        self.NUM_MACHINES = 1
        self.NUM_REGULAR_LINES = 1
        self.NUM_FREQUENT_LINES = 1
        self.NUM_AUTOMATED_LINES = 1

        # distribution of group sizes
        self.SIZES = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5]

        # points per diamond
        self.DIAMOND_COST = 10

        # print settings
        self.SILENT = False
        self.DELAY = 0.25  # seconds

        self.check_in_count = 0
        self.diamond_count = 0

    def setup(self):
        """ Set up the game by spawning Entities according to the options """

        self.print_state("initializing game...")

        self.spawn_counter(self.NUM_COUNTERS)
        self.spawn_machine(self.NUM_MACHINES)
        self.spawn_line_regular(self.NUM_REGULAR_LINES)
        self.spawn_line_frequent(self.NUM_FREQUENT_LINES)
        self.spawn_line_automated(self.NUM_AUTOMATED_LINES)

        self.spawn_agent(self.NUM_AGENTS)
        self.spawn_supervisor(self.NUM_SUPERVISORS)
        self.spawn_group(self.NUM_GROUPS)

        self.print_state("finished initializing game")

    def spawn_counter(self, amount=1):
        """ Add necessary Counters to the master list """
        for _ in xrange(amount):
            counter = Counter()
            GSM.counters.append(counter)
            self.print_state("spawned %s" % counter)

    def spawn_machine(self, amount=1):
        """ Add necessary Machines to the master list """
        for _ in xrange(amount):
            machine = Machine()
            GSM.machines.append(machine)
            self.print_state("spawned %s" % machine)

    def spawn_line_regular(self, amount=1):
        """ Add necessary Regular Lines to the master list """
        for _ in xrange(amount):
            line = Line(frequent=False)
            GSM.lines_regular.append(line)
            self.print_state("spawned %s" % line)

    def spawn_line_frequent(self, amount=1):
        """ Add necessary Frequent Lines to the master list """
        for _ in xrange(amount):
            line = Line(frequent=True)
            GSM.lines_frequent.append(line)
            self.print_state("spawned %s" % line)

    def spawn_line_automated(self, amount=1):
        """ Add necessary Automated Lines to the master list """
        for _ in xrange(amount):
            line = Line(frequent=False, automated=True)
            GSM.lines_automated.append(line)
            self.print_state("spawned %s" % line)

    def spawn_agent(self, amount=1):
        """ Add necessary Agents to the master list """
        for _ in xrange(amount):
            agent = Agent(GSM.counters, GSM.machines,
                          GSM.lines_regular, GSM.lines_frequent)
            GSM.agents.append(agent)
            self.print_state("spawned %s" % agent)

    def spawn_supervisor(self, amount=1):
        """ Add necessary Supervisors to the master list """
        for _ in xrange(amount):
            supervisor = Supervisor(GSM.counters, GSM.machines)
            GSM.supervisors.append(supervisor)
            self.print_state("spawned %s" % supervisor)

    def spawn_group(self, amount=1):
        """ Add necessary PassengerGroups to the master list """
        for _ in xrange(amount):
            passengers = []
            for _ in xrange(choice(self.SIZES)):
                passengers.append(Passenger())
            group = PassengerGroup(passengers, GSM.lines_regular,
                                   GSM.lines_frequent, GSM.lines_automated,
                                   GSM.machines)
            GSM.groups.append(group)
            group_members = '\n\t'.join(str(p) for p in passengers)
            self.print_state("spawned %s:\n\t%s" % (group, group_members))

    def prompt_actors(self, actors):
        """
        Call all Actors to act, print their actions,
        remove Actors once their roles are finished
        """
        for actor in actors:
            action = actor.act()
            if action:
                self.print_state(action, str(actor))
                if action.startswith("checked in"):
                    self.check_in_count += 1
                elif action.startswith("finished using"):
                    actors.remove(actor)

    def print_state(self, message, caller="Game Manager"):
        """ Print the provided message as the provided caller """
        if not self.SILENT:
            print(caller + " " + message)
            sleep(self.DELAY)

    def tick(self):
        """
        Execute the next game tick:

        Involves prompting all Actors, calculating diamond rewards,
        and spawning PassengerGroups randomly
        """
        
        self.prompt_actors(self.groups)
        self.prompt_actors(self.agents)
        self.prompt_actors(self.supervisors)

        if self.check_in_count >= self.DIAMOND_COST:
            self.check_in_count -= self.DIAMOND_COST
            self.diamond_count += 1
            self.print_state("reports %d diamonds earned"
                             % self.diamond_count)

        # spawn a new group at a 50/50 rate
        if getrandbits(1):
            self.spawn_group()
