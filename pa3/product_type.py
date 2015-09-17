# Kevin Nash (kjn33)
# EECS 293
# Assignment 2

from enum import Enum

class ProductType(Enum):
    """Allow instantiation of predetermined products in the style
    of an enum.
    """
    OPOD = "oPod"
    OPAD = "oPad"
    OPHONE = "oPhone"
    OWATCH = "oWatch"
    OTV = "oTv"
