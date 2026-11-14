# This comiles.
# This won't raise an error until executed.
# This shows that python compiler cannot be depended upon
def bad_reference():
    # This function contains a bad reference to a variable that is not defined
    print(
        undefined_variable
    )  # This will raise a NameError because undefined_variable is not defined
    undefined_variable = (
        "This variable is now defined"  # Defining the variable after its usage
    )


# bad_reference()  # Calling the function to demonstrate the bad reference


def sommetimes_ok(x):
    if x:
        my_var = 123
    print(my_var)


# This will print 123 because my_var is defined in the if block
# sommetimes_ok(True)

# This will raise a UnboundLocalError because my_var is not
# sommetimes_ok(False)


# This also compiles but will raise an error when executed
def bad_math():
    return 1 / 0


# bad_math()


# This will also compile but will raise an error when executed
# Undefined function call
# hi_method()


def add_method(a, b):
    return a + b


# This will also compile but will raise an error when executed
# TypeError
add_method(1)
