# Kevin Nash (kjn33)
# EECS 293
# Assignment 4

import abc
from request_error import RequestError
from request_status import RequestStatus

class Request(object):
    """Function like an interface"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        """Enforce the abstract quality of Request"""
        raise NotImplementedError("class Request cannot be instantiated")

    def process(self, product, status):
        raise NotImplementedError("subclasses must implement process")
