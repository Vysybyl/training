import unittest
# ===
#  LESSON 4 - CLASSES AND OBJECTS
# ===

# Classes are programming element that somehow sum up and enhance all the elements seen so far.
# Their usage is widespread as they are the base of many programming languages such as Java or C#.
# They are also one of the most difficult concept to grasp when learning how to code.

# Object-oriented programming (OOP) is the programming paradigm that uses classes and objects.

# First, let's consider a real-life problem. Imagine that you need to model a group of animals:
# a horse, a duck, a rooster and a dog.
# Every animal has a name, a call and a way of moving. For instance, the duck flies and the dog barks.
# We'll need two functions to make the animal call and move.

# Let's try to do it with what we know so far. A possible implementation would be the following:

dog_name = "Fido"
dog_call = "woof"
dog_move = "runs"

duck_name = "Donald"
duck_call = "quack"
duck_move = "flies"

rooster_name = "Chad"
rooster_call = "cock-a-doodle-doo"
rooster_move = "walks"

horse_name = "Black"
horse_call = "neigh"
horse_move = "gallops"

# Well, we already have 12 variables to juggle with. Now let's look how the make_call() function:
def make_call(animal_name):
    if animal_name == dog_name:
        print dog_name + " says: " + dog_call
    elif animal_name == duck_name:
        print duck_name + " says: " + duck_call
    elif animal_name == rooster_name:
        print rooster_name + " says: " + rooster_call
    else:
        print horse_name + " says: " + horse_call


# If tomorrow we'd needed to add a new animal (let's say a fish) we'd need to add three more variables and to
# add an 'elif' clause in the above function.
# Wouldn't it be great to have a way to define an 'abstract' animal, with general characteristics (name, call and move)
# and to use that same code for every specific animal we need to model?

# This is one of the reason we use classes. Here's the example of an Animal class:

class Animal(object):  # one way to define a class in python.

    def __init__(self, animal_name, animal_call, animal_move):  # This is a function defined inside a class. We call it a method.
        self.name = animal_name  # We are assigning to 'self.name' the value 'animal_name'
        self.call = animal_call
        self.move = animal_move

    def make_call(self):  # This is another method. We'll use it to print the animal's call
        print self.name + " says: " + self.call  # NOTE that we are using the self.XXX variables defined above. (They are called properties)

    def make_move(self):  # and finally to move...
        print self.name + " " + self.call


# Now let's use the class to create animals:
a_dog = Animal("Fido", "woof", "runs")
a_duck = Animal("Donald", "quack", "flies")
a_fish = Animal("Nemo", "...", "swims")

# and to make them act:
a_dog.make_call()  # This is a method call. It will execute the code above for the properties defined
                   # for this object ("Fido", "woof", "runs"). It will print "Fido says: woof"

a_duck.move()  # prints "Donald flies"
a_fish.make_call()  # prints "Nemo says ..."

# NOTE - The 'self' is an abstract way to refer to the object itself (in our case a generic animal) without
# any other specification

# NOTE - The __init__ method is called when the object is created. It's called a class constructor.

# ===
#  EXERCISE 4
# ===

# Define a class called Food.
# The class initializer will receive a food_name (str) and a cooking_time (int) in minutes.
# The class will have two methods: one called 'cook' and one called 'taste'
# The 'cook' method will return the sentence "You will need X minutes", where X is the cooking time
# The 'taste' method will return the sentence "This Y are yummy!", where Y is food name.


class MyTestCase(unittest.TestCase):
    def test_three(self):
        lasagne = Food("lasagne", 30)
        noodles = Food("noodles", 5)
        self.assertTrue(lasagne.cook() == "You will need 30 minutes")
        self.assertTrue(lasagne.taste() == "This lasagne are yummy!")
        self.assertTrue(noodles.cook() == "You will need 5 minutes")
        self.assertTrue(noodles.taste() == "This noodles are yummy!")

if __name__ == '__main__':
    unittest.main()



