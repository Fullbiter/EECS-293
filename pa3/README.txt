Kevin Nash (kjn33)
EECS 293
Assignment 3

I.  Instructions

    A.  Running test_suite.py will run unit tests.

    B.  You may also test classes directly by importing
        their modules and instantiating them.

II. Explanation of Design Choices

    A. General
        1.  All "getter" methods that are specified in the assignment but
            do not appear in this code are purposefully omitted because
            their function is accomplished with attribute access.

        2.  The assignment's specification for package-private constructors
            is ignored by this code, as the Python language does not
            feature such access control.

    B.  Product class

        1.  product.py has been removed from the package,
            as its intended use as an interface is unnecessary.

    C.  ProductType class

        1.  A get_name() method is not included, as its function is
            accomplished with a ProductType.<constant>.value call.

    D.  ProductError class

        1.  ProductError is named as such rather than as ProductException
            in adherence with Python's naming convention for exceptions.
            i.e. <SomeError>(Exception)

        2.  The enum constants are given numerical values as a default
            because the assignment doesn't give any specification for them.

    E.  SerialNumber class

        1.  is_zero() is used in both is_even() and is_odd() because
            zero is neither even nor odd. Before this change, a
            serial number of 0 was found to be valid for Opod objects.
