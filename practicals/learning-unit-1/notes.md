# Lists

In Python, a list is a mutable sequence of elements enclosed in square brackets. It can contain elements of different data types, such as numbers, strings, or even other lists. Lists are versatile and allow for dynamic modification, such as adding, removing, or changing elements. Here are a few examples of lists:

1. Empty list:
`empty_list = []`

2. List with elements:
`numbers = [1, 2, 3, 4, 5]`

3. List with mixed data types:
`mixed_list = [1, 'apple', True, 3.14]`

4. Accessing list elements:
`print(numbers[0]) # Output: 1`

5. Modifying list elements:
`numbers[0] = 10`
`print(numbers) # Output: [10, 2, 3, 4, 5]`

6. Adding elements to a list:
`numbers.append(6)`
`print(numbers) # Output: [10, 2, 3, 4, 5, 6]`

7. Removing elements from a list:
`numbers.remove(3)`
`print(numbers) # Output: [10, 2, 4, 5, 6]`

Lists are commonly used when you need to store and manipulate collections of data. They provide flexibility and functionality for various operations, such as sorting, searching, and iterating over elements.

# Tuples

In Python, a tuple is an immutable sequence of elements enclosed in parentheses. It can contain elements of different data types, such as numbers, strings, or even other tuples. Tuples are similar to lists, but unlike lists, they cannot be modified once created. Here are a few examples of tuples:

1. Empty tuple:
`empty_tuple = ()`

2. Tuple with single element:
`single_tuple = (42,)`

3. Tuple with multiple elements:
`fruits = ('apple', 'banana', 'orange')`

4. Accessing tuple elements:
`print(fruits[0]) # Output: 'apple'`

# Sets

In Python, a set is an unordered collection of unique elements. It is defined by enclosing the elements within curly braces `{}` or by using the `set()` function. Sets are useful when you want to store a collection of items without any duplicates and perform operations like union, intersection, and difference efficiently. Here are a few examples of sets:

1. Creating a set:
python
   my_set = {1, 2, 3, 4, 5}
   


2. Adding elements to a set:
python
   my_set.add(6)
   my_set.update([7, 8, 9])
   


3. Removing elements from a set:
python
   my_set.remove(3)
   my_set.discard(4)
   


4. Set operations:
python
   set1 = {1, 2, 3}
   set2 = {3, 4, 5}

   union_set = set1.union(set2)  # {1, 2, 3, 4, 5}
   intersection_set = set1.intersection(set2)  # {3}
   difference_set = set1.difference(set2)  # {1, 2}
   


5. Checking membership:
python
   if 2 in my_set:
       print("2 is in the set")
   


Sets are commonly used when you need to store a collection of unique elements and perform operations like checking membership, finding intersections, or removing duplicates efficiently.