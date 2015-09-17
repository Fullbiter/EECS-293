# Kevin Nash (kjn33)
# EECS 293
# Assignment 3

from opod import Opod
from opad import Opad
from ophone import Ophone
from owatch import Owatch
from otv import Otv
from product_type import ProductType

class Factory(Enum):
    @staticmethod
    def make(product_type, serial_number, description=None):
        """"""

        if product_type.is_valid_serial_number(serial_number):
            return True
