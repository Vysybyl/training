import unittest
# ===
#  LESSON 3 - FUNCTIONS AND CONTROL STRUCTURES
# ===

# Imagine that you have to perform the same operation several times in your code.
# For instance, you need to calculate the area of a triangle given the base and height.
# Instead of repeating the formula using the operators all the times, you can define a function:

def area_of_triangle(base, height):  # def <NAME OF THE FUNCTION>(ARGUMENTS):
    result = (base * height) / 2.0  # apply the formula
    return result  # return the answer

# So, next time you need to get the area, you just need to call the function
area = area_of_triangle(3, 4)  # area will be assigned the value 6

# Can't we do anything else apart from math, string and list operations? Of course we can!
# To do so we need control structures.

# A control structure is a way to define when a group of lines of code (a block) will be called (executed)
# The most simple control structure is the if... else statement:

# Just if
if 4 < 5:
    print "I know how to compare numbers!"

# if...else
if "Parrot" != "parrot":
    print "python is case-sensitive"
else:
    print "python is not case-sensitive"

# The code indented under the 'if' will be executed only if the condition is true. Otherwise, the code
# under 'else' will run.

# Let's put it all together: the following function receives one argument.
# If the argument is a non-empty list, it prints the first element.
# Otherwise, if it is an int, it will print the message "I like integers!".
# Otherwise, it will print "Not an int nor a list"
# Finally it will print "Function ended"


def first_function(arg):
    if type(arg) is list and len(list) > 0:
        print list[0]
    elif type(arg) is int:
        print "I like integers!"
    else:
        print "Not an int nor a list"
    print "Function ended"

first_function(['one', 'list', '!'])
# one
# Function ended
first_function(321654)
# I like integers!
# Function ended
first_function("span")
# Not an int nor a list
# Function ended
first_function(None)
# Not an int nor a list
# Function ended


# ===
#  EXERCISE 3
# ===

# Define a function called my_fun that receives one argument and
# - returns "Ping" if the argument is an even number
# - returns "Pong" if the argument is a multiple of 3
# - returns "Ping Pong" if the argument is even and a multiple of 3
# - if the argument is a dictionary with the key "yummy", returns the value under that key.


class MyTestCase(unittest.TestCase):
    def test_three(self):
        self.assertTrue(my_fun(20) == "Ping")
        self.assertTrue(my_fun(15) == "Pong")
        self.assertTrue(my_fun(18) == "Ping Pong")
        t_dict = {"yummy": "lasagne!"}
        self.assertTrue(my_fun(t_dict) == "lasagne!")

if __name__ == '__main__':
    unittest.main()



