# Kevin Nash (kjn33)
# EECS 293
# Assignment 2

class ProductType:
    """Allow instantiation of predetermined products in the style
    of an enum.
    """
    OPOD = "oPod"
    OPAD = "oPad"
    OPHONE = "oPhone"
    OWATCH = "oWatch"
    OTV = "oTv"

    def __getattr__(self, name):
        """Restrict ProductType instantiation to only enumerated types"""
        if name in self:
            return name
        raise AttributeError