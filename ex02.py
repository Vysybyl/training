import unittest
# ===
#  LESSON 2 - TYPES
# ===

# In the previous lesson we've assigned values to different variables.
# We've used values of different types. To know which type an element of code is
# we can use the 'type()' function. Like this:

type(23)  # Returns int that means integer
type(12.2)  # float
type("Blah")  # str
type('Bleh')  # str

var1 = "a variable"
type(var1)  # str
type(True)  # bool, that means boolean

# Sometimes you can transform a type into another. That's called casting:
type(str(12.34))  # str
type(float('12.34'))  # float
type(int(0.0001))  # int
type(2 < 3.0)  # bool

# Two very useful types in python are lists and dictionaries.

# Lists
a_list = [12,  'piece of text', 35.203, 100, 100]
an_empty_list = []
another_empty_list = list()

# A list is a collection of ordered values. It can contain anything, including other lists

# You can access elements or parts of a list using indexing or slicing (we'll skip slicing for now)

lst = ["first", "second", "third"]
lst[0]  # first - NOTE that the first index is 0
lst[2]  # third

# By the way, you can add list together with '+' !
head = ['hey', "ho"]
tail = ["let's", "go"]
head + tail  # ['hey', "ho", "let's", "go"]

# Dictionaries
a_dict = {'name': 'paul', 'age': 25, "favourite_color": "red", 1: "the key is an integer!"}
an_empty_dict = {}
another_empty_dict = dict()

# A dictionary is a collection of key-value pairs. If you know the key, you can access the value with:
a_dict['name']  # paul
a_dict[1]  # the key is an integer!


# ===
#  EXERCISE 2
# ===

# From now on, we'll use python test framework to check the exercise. If everything is correct, the test will pass
# otherwise, it will fail.
# Answer by writing your code below

# Create a list of 4 elements called my_list. The first one must be an int, the last one must be a float

# Define a dictionary called my_dict that contains the keys "odd" and "even".
# The values must be an odd and an even number (integer)


class MyTestCase(unittest.TestCase):
    def test_two(self):
        self.assertTrue(len(my_list) == 4)
        self.assertTrue(type(my_list[0]) is int)
        self.assertTrue(type(my_list[3]) is float)

        self.assertTrue(my_dict["odd"] % 2 != 0)
        self.assertTrue(my_dict["even"] % 2 == 0)

if __name__ == '__main__':
    unittest.main()



