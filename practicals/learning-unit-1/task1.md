# Learning Unit 1: Task 1

# Data Types and Structures

We need to start by building up our understanding of data types. These are fairly simple when we discuss the common data types, but as we start to model these using data structures this can be more involved.

In addition to our resources, You can work through the Khan Academy and W3 schools interactive exercices if you do not feel you have a confident understanding of storing basic data types in variables yet.

Here's a little test for yourself - if you can't do this, explore the resources above and discuss with your tutors until this makes sense:

Write a simple program that:
- Defines a variable with your favorite number and prints it
- Stores a greeting in a string and prints it
- Stores a boolean value representing whether Python is fun and prints it
- Stores a list of your three favorite colors and prints the list
- Creates a dictionary with your name and age, then prints it.
- Stores a pair of coordinates in a tuple and prints them.


If you cannot do these keep working on understandin these concepts.

## Task 1 : Compare Game

In this challenge we are going to make a stats generator for a 'top trumps' type game system. Remember that what really defines a game like this is creativity so enjoy and have fun playing around. We can make character stats for anything you might be interested in and could be inspired by something real world you are interested in.

Some ideas could be:
- to represent a set of sports characters
- create your own models of cars/vehicles
- Dungeons and dragons inspired characters

Start by creating a dictionary structure for the stats you want to display. Use appropriate data types to represent the property you are demonstrating. For example we may use a number to represent someones 'top speed' or reaction time. A name or item in an inventory is best represented with a string. A boolean could be used to indicate specific and important characteristics, for example if a character is the 'main character'

Here I've designed one as an example: 

```python

character = {
    "name": "Thalor the Swift",              # string
    "class": "Rogue",                        # string
    "level": 5,                              # integer
    "speed": 32.5,                           # float (feet per second)
    "is legendary": True,                    # boolean
    "inventory": ["dagger", "cloak", "map"], # list of strings
    "abilities": {
        "stealth": 9,
        "lockpicking": 8,
        "acrobatics": 7
    }                                        # nested dictionary
}

```

### Make some data sets

Once you have designed your data structure, make around 10-15 different data structures to represent your characters. Populate the data in each field of the struct with values you think are appropriate. Structure things as a list that we can make into a game later.

For Example: See `nathans-characters.py`

### Make a simple top trumps game

There is some code you can use in the file `compare_game.py`.
Have a play around getting that running. 

If you search on the word 'todo' you will see some key bits of code that you can can modify to tailor the game to your idea.

In particular, there are issues with the `compare_stats()` function which does not effectively do any meaningful comparison.
For example, the class with the longest string wins when stats with strings are picked, which does not seem very intersing...

Copy this code and modify it to work with your characters and ideas.
