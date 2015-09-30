Kevin Nash (kjn33)
EECS 293
Assignment 4

I.  Instructions

    A.  Running test_suite.py will run unit tests.

    B.  You may also test classes directly by importing
        their modules and instantiating them.

II. Explanation of Design Choices

    A.  Exchange class

        1.  Unlike other getter methods, get_compatible_products() is
            necessary and implemented to prevent unwanted mutation
            of the compatible_products attribute.

    B.  Exchange.Builder class

        1.  The assignment specifies that the nested Builder class be static.
            While there is no formal "static" declaration, referring to the
            class directly provides the same functions as a static decorator.
            i.e. Exchange.Builder()

        2.  See A.1

    C.  RequestError class

        1.  RequestError is named as such rather than as RequestException
            in adherence to Python's naming convention for exceptions.
            i.e. <SomeError>(Exception)

    D.  SerialNumber class

        1.  __hash__ was implemented so that SerialNumbers can be added to sets.

    E.  Products

        1.  The request type is checked and handled within process(),
            as the Python language does not feature method overloading.

III. Explanation of Previous Design Choices

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
            in adherence to Python's naming convention for exceptions.
            i.e. <SomeError>(Exception)

        2.  The enum constants are given numerical values as a default
            because the assignment doesn't give any specification for them.

    E.  SerialNumber class

        1.  is_zero() is used in both is_even() and is_odd() because
            zero is neither even nor odd. Before this change, a
            serial number of 0 was found to be valid for Opod objects.
