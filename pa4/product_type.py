# Kevin Nash (kjn33)
# EECS 293
# Assignment 3

from enum import Enum

class ProductType(Enum):
    """Enumerate various product types."""
    
    OPOD = "oPod"
    OPAD = "oPad"
    OPHONE = "oPhone"
    OWATCH = "oWatch"
    OTV = "oTv"

    # get_name() is simply ProductType.<constant>.value