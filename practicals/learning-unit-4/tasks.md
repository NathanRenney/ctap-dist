# Week 14 Tasks for practicals

# Task 1 : Error handling
## 1.1 : Return values

Read through and run the following code. Here we demonstrate a simple program that manages errors as a returned boolean value, and how we might use this code. We use the input function to simulate getting user info and then call our function to add them to our list of party attendees. This function can fail however due to inviting someone who is under 18.

Run the following code, explore the possibility of adding another failure condition by banning people named 'simon' and 'marshall'. You should only edit the function! You should then be able to run this code and get appropriate messages (using the names simon or marshall should cause an error no matter what age you provide).

```python
# A list of people currently invited to the party
party_goers = ['jake', 'marceline']

# A function to add to the party (returns true on success or false on failure)
def invite_to_party(name, age):
    if age < 18:
        return False
    else:
        party_goers.append(name)
        return True

# Code to simulate our invite, handling errors as appropriate
n = input("Enter your name: ")
a = int(input("Enter your age: "))

if invite_to_party(n,a):
    print('Invited ' + n + ' to the party')
else:
    print('Error ' + n + ' could not be added to the party')        

```

> You can check out the section in the notes.md for this week which covers advanced strategies for working with return values. 
## 1.2 : Exceptions


If you have a solution for Week 12 task 3, extend that work to raise an exception when a package is attempted to be delivered but the package count is negative. 

If you have not got an existing solution for week 12 task 3 then you can attempt the following problem:

Write a program that prompts the user to enter their age. If the age entered is less than 18, raise a custom exception called "UnderAgeException". Handle the exception and display an appropriate error message.

	Example Output:
	Enter your age: 15
	UnderAgeException: You must be at least 18 years old to proceed.
	
	Enter your age: 25
	You are eligible to proceed.

To complete this task, the beginner Python user needs to write the code for handling the "UnderAgeException" and display the appropriate error message when the age entered is less than 18.

# Task 2 : (Assessment work) 

## 2.1

Identify and discuss potential errors in the problem you have identified for your scenario and write this up in approximately 150 words. For this section, focus on a range of errors and why they are important to be handled; which ones may be high priority for example. What are the acceptable means of failure? 

## 2.2

Choose an error handling strategy (either return values or exceptions for example) and implement an example of how you might add error handling in python code, in relation to your problem. Create a small simulation of this error handling strategy and then document your approach in a further 150 words. Discuss your choice for using either return values or exceptions and how you intended the error to be handled.

> Tip: if you are finding this hard to start look at the style of code used in Task 1.1 for inspiration. Note that return value errors may be simpler to work with and produce simpler control flow, however they may not provide as much insight as strategies like exceptions.

# Task 3

## 3.1 : Unit tests

> Note: in this task, we will use some code constructs that have not been introduced yet. Use the example code as a framework and we will explore the use of import and asserts for example in future sessions.

In the lecture we have discussed different testing strategies. For more practical exploration we will focus on unit testing. Python has a built in module for unit testing. Here's an example of it's use, by  importing the built-in `unittest` module in Python:

```python
import unittest

# The function in your code to be tested
def add_numbers(a, b):
    return a + b

# Create a test case class, containing functions for each test
class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)

    def test_add_zero_to_number(self):
        result = add_numbers(5, 0)
        self.assertEqual(result, 5)

# Run the tests
unittest.main()
```

In this example, we have a function `add_numbers` that adds two numbers. We write test cases for this function using the `unittest.TestCase` class. Each test case is defined as a method that starts with the word "test". Inside each test method, we call the function with different inputs and use assertions to verify that the expected result matches the actual result.

To run the tests, we use the `unittest.main()` function, which discovers all the test cases defined in the file and runs them.

When you run this script, the output will show whether the tests pass or fail. If all the assertions pass, you'll see an output like this:

```markdown
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

If any assertion fails, you'll see a detailed error message indicating which test case failed and what the expected and actual results were.

**Run and test the above code and make a change in the add_numbers function to cause the test cases to fail.**
## 3.2

Add two more test functions to the example above to test for adding zero to zero and another for adding a negative and a positive. 

# Task 4 (Assessment work)

## 4.1

Choose a function from the code around your scenario and write a unit test that tests the function in as many ways as you can think of. Try to focus on a function that can possibly fail in more than one way.

In your report document and discuss this unit test, describing what each test checks and how this is checked (approximately 150 words).
## 4.2 

Discuss further how other testing strategies can applied to your problem. What components require particular forms of testing and how can this help to ensure that your problem can be solved.
