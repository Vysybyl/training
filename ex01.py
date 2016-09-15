# Hi! This is a very short introduction to (python) programming.


# You may wonder why I'm starting the line with a '#' sign.
# ...well, the '#' is used in python to mark a comment line.
# That is, a line that will not be read by the computer as par of
# your code.


# You can also use '#' at the end of your code line:
this_is_a_piece_of_code = 0  # this is just a comment


# By pressing 'Ctrl' + '/' in PyCharm you will comment (or uncomment) the line you are in
# ----- Try it on this line! -----

"""
To comment several lines at once
You can use three quotes. (But they are generally used for documentation)
"""


# ===
#  LESSON 1 - VARIABLES
# ===

# A variable is an element of code used to store a value.
# It works like a placeholder, as the 'x' in a mathematical equation

# It can be (almost) any sequence of characters,
# You can assign a value to a variable using the '=' sign
# From that line on, all the times you call the variable names, the computer
# will 'read' it as the assigned value

a_variable = 2
another_variable = 135483927
x = 60.234

# TIP: Use the python interpreter to play around with variables.

# A variable can also contain text. We call it a 'string'
a_string_variable = "Hey! This is not a number"
another_string = "4"  # NOTE that this is a string, not a number!
one_more = 'yep... this is also a string. (it contains eleven words)'

# Now that we have variables, let's do something with them!
# One of the most basic usage of programming is to do math operations:

a = 3
b = 2
c = a + b  # c is now 5!

a * b  # 3 * 2 = 6
a - 1  # 3 - 1 = 2
a / b  # NOTE that this is rounded down to 1
# If you want decimals (called 'floats') use the dot:
6.0 / 2.0  # this returns 3.0
a / 2.0  # this returns 1.5

# You can re-use the same variable by assigning it another value:

k = 2
k = 1000  # k is now 1000
k = 2 - 1  # k is now 1
k = k + 3  # k is now 4

# The + - / * and = signs are called operators. + and * can be used on strings too. Try them out!



# ===
#  EXERCISE 1
# ===

# Do not pay much attention to the structure below yet.
# Just follow the instructions and
# Remember to
#   INDENT the code
# as a bonus, you'll learn how to use the print function!

def run():
    print "TEST STARTED!"
    # Create a variable called my_var and assign to it the value 10

    print "The value of 'my_var' is " + str(my_var)

    # Add  divide my_var by 10.0 and print the result

    # Create a variable called my_string and assign to it the value 'python is cool!'

    # Print the variable

    # Multiply my_string by my_var and print the result







if __name__ == '__main__':
    run()


