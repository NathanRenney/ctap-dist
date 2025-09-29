# Exceptions

Here's a brief example of how to use exceptions in Python:

```python
try:
    # Attempt to perform some operation that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception that was raised
    print("Error: Division by zero is not allowed.")
except Exception as e:
    # Handle any other exceptions that were not caught by the previous except block
    print("An error occurred:", str(e))
else:
    # Code to be executed if no exceptions were raised
    print("The result is:", result)
finally:
    # Code that will always be executed, regardless of whether an exception was raised or not
    print("Program execution has finished.")
```

In this example, we attempt to divide the number 10 by 0, which is not allowed and will raise a `ZeroDivisionError`. We then use a `try-except` block to catch and handle this specific exception. If any other exception is raised, the program will catch it in the `except Exception as e` block. The `else` block is executed if no exceptions were raised, and the `finally` block is always executed, regardless of whether an exception was raised or not.

To explore python exceptions in more depth here are some external resources. In particular, you might consider a component of this course from LinkedIn courses (which you can access using your UWE account):
[Linked in Learning - Python Exceptions](https://www.linkedin.com/learning/python-essential-training-18764650/errors-and-exceptions?resume=false&u=56744785)

### Alternate resources

- [Python Docs](https://docs.python.org/3/tutorial/errors.html)
- [Python Error handling with exceptions (youtube)](https://www.youtube.com/watch?v=NIWwJbo-9_8)
- [Advanced exceptions (youtube)](https://www.youtube.com/watch?v=ZUqGMDppEDs)

# Return Values

Here's an example of a function that divides a number by another number, using three arguments to manage the 'data' and a return value for error handling:

We can see this has some limitations in 'ergonomics' as we can no longer compose functions as they return errors.

```python
def divide_numbers(dividend, divisor, result):
    if divisor == 0:
        return False
    else:
        result[0] = dividend / divisor
        return True
```

In this function, we check if the divisor is zero. If it is, we return `False` to indicate that the division cannot be performed. Otherwise, we calculate the result by dividing the dividend by the divisor and modify the `result` argument using reference.

Here's  examples of how you can use this function:

### Initialise the variables
```python
dividend = 10
divisor = 2
result = [0]  # Using a list to pass the result by reference
```
### Call the function
```python
success = divide_numbers(dividend, divisor, result)
```
### Check the result

```python
if success:
    print("Division successful!")
    print("Result:", result[0])
else:
    print("Cannot divide by zero!")
```

In this example, we attempt to divide `dividend` (10) by `divisor` (2). Since the division is possible, the `result` list is modified with the calculated result. The `success` variable is `True`, so we print the successful division result. If the divisor were zero, the function would return `False`, and we would print the "Cannot divide by zero!" message.
```
```
# Advanced return values (Option Types)

In Python, there is no built-in implementation of an Option type like in some other programming languages. However, we can create a simple implementation of an Option type using classes. Here's an example:

```python
class Option:
    def __init__(self, value):
        self.value = value
        self.has_value = True
    
    def is_some(self):
        return self.has_value
    
    def is_none(self):
        return not self.has_value
    
    def get(self):
        if self.has_value:
            return self.value
        else:
            raise ValueError("Option is None.")
    
    @staticmethod
    def some(value):
        return Option(value)
    
    @staticmethod
    def none():
        return Option(None)
```

In this implementation, we have a class called `Option` that represents an option type. It has an instance variable `value` to store the actual value and a boolean `has_value` to indicate whether the option has a value or is None.

The class provides methods like `is_some()` and `is_none()` to check if the option has a value or is None. The `get()` method returns the value if it exists, otherwise it raises a `ValueError`.

We also have static methods `some()` and `none()` to create instances of the Option class with a value or as None.

Here's an example usage:

```python
# Creating options
option1 = Option.some(10)
option2 = Option.none()

# Checking if options have values
print(option1.is_some())  # Output: True
print(option2.is_none())  # Output: True

# Getting values from options
print(option1.get())  # Output: 10
try:
    print(option2.get())  # Raises ValueError: Option is None.
except ValueError as e:
    print(str(e))
```

In this example, we create two options, one with a value of 10 and another as None. We then check if the options have values using the `is_some()` and `is_none()` methods. Finally, we retrieve the values using the `get()` method, and handle the case when the option is None by catching the `ValueError` exception.

# Unit tests

Here's an example of how you can write unit tests for a function that checks if a user has a valid email using the `unittest` module in Python:

```python

import unittest

# Function to be tested
def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

# Test case class
class TestIsValidEmail(unittest.TestCase):

    def test_valid_email(self):
        result = is_valid_email("test@example.com")
        self.assertTrue(result)

    def test_invalid_email_no_at_symbol(self):
        result = is_valid_email("testexample.com")
        self.assertFalse(result)

    def test_invalid_email_no_dot(self):
        result = is_valid_email("test@examplecom")
        self.assertFalse(result)

    def test_invalid_email_no_at_symbol_and_dot(self):
        result = is_valid_email("testexamplecom")
        self.assertFalse(result)

# Run the tests
unittest.main()
```

In this example, we have a function `is_valid_email` that checks if an email contains both an "@" symbol and a "." symbol. We write test cases for this function using the `unittest.TestCase` class. Each test case is defined as a method that starts with the word "test". Inside each test method, we call the function with different inputs and use assertions to verify that the expected result matches the actual result.

## A note on Asserts

The `unittest` module in Python provides several 'assert' functions that are used within test cases to check conditions and make assertions about the behavior of the code being tested. Here are some commonly used assert functions in `unittest`:

1. `assertEqual(a, b)`: This function checks if `a` is equal to `b`. If the values are not equal, an assertion error is raised.

2. `assertTrue(x)`: This function checks if `x` is true. If `x` evaluates to false, an assertion error is raised.

3. `assertFalse(x)`: This function checks if `x` is false. If `x` evaluates to true, an assertion error is raised.

4. `assertIs(a, b)`: This function checks if `a` is the same object as `b`. If the objects are not the same, an assertion error is raised.

5. `assertIsNot(a, b)`: This function checks if `a` is not the same object as `b`. If the objects are the same, an assertion error is raised.

6. `assertIsNone(x)`: This function checks if `x` is None. If `x` is not None, an assertion error is raised.

7. `assertIsNotNone(x)`: This function checks if `x` is not None. If `x` is None, an assertion error is raised.

8. `assertIn(a, b)`: This function checks if `a` is a member of `b`. If `a` is not in `b`, an assertion error is raised.

9. `assertNotIn(a, b)`: This function checks if `a` is not a member of `b`. If `a` is in `b`, an assertion error is raised.

10. `assertRaises(exception, callable, *args, **kwargs)`: This function checks if calling `callable(*args, **kwargs)` raises an exception of the specified type `exception`. If the exception is not raised, an assertion error is raised.

These assert functions, along with others provided by `unittest`, help in writing expressive and comprehensive test cases to verify the correctness of your code.