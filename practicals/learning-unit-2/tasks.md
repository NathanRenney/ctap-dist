# Week 15 Tasks for practicals

# Task 1 : 
## 1.1 

Write functions that take a single parameter and perform the following operations on it, then return that value:
- half the number provided
- double the number provided
- subtract one from the number provided
- square the number provided
- append the string '.'
- prepend the string 'answer: '

## 1.2

Example (assuming your have defined the previous functions):

take 5, double it, subtract 1, prepend the string 'answer: '
`print(prepend_answer(subtract_one(double_it(5))))`
> nb. this may vary based on what you named your function

Use function composition to solve and print the following problems:
- take 11, double it, double it, prepend the string 'answer', append the '.'
- take 1024, half it, half it, half it, square it
- take 1, double it, square it, subtract 1, prepend the string 'answer'

## 1.3
Create a class called Rectangle that represents a rectangle shape.  
The class should have attributes for width and height, and methods to calculate the area and perimeter of the rectangle.  

You should then be able to test this class with the following code:
```python
# Test the Rectangle class  
rectangle = Rectangle(5, 3)  
print("Width: ", rectangle.width)  
print("Height: ", rectangle.height)  
print("Area: ", rectangle.calculate_area())  
print("Perimeter: ", rectangle.calculate_perimeter())
```

# Task 2 (Assessment work)

Considering code that you have written so far, describe the use of programming constructs or patterns that you have used and attempt to identify where strategies such as those discussed in the lecture can be applied. 
For example, you may identify that print statements could be better placed by focusing on returning values throughout your code and then printing in one place, imitating the MVC pattern. 

You may also observe places where function composition or classes might be a useful programming construct for a part of your problem. 

In this section, you could also discuss where these ideas might be relevant in code that you haven't written. Classes in particular often help to build up representations of real world things that contain both behaviour and data and you might suggest some examples of this in relation to your problem. Bonus points if you write some of the class as a snippet!

What other 'best practices' have you discovered or learned that you have attempted or are attempting to apply in your work?

# Task 3 (Assessment work)

For this task we want to begin evaluating your work in preparation for the final section of your report. **Even if you are not finished with the rest *complete this task!***
This will give you something to build upon...

Task: Using bullet points document 4-8 challenges that you faced in the process of this module. Engage your practical tutor and/or peers in discussion and create sub points that indicate what was challenging, how you overcame the challenge and/or what you would do differently next time for this challenge.

This take the form of something similar to this:

 - Decomposition of the initial scenarios problem was challenging as it was hard to know where to start.
	- Discussed the problem with peers
	- started with a broad definition of the problem and added lots of initial sub problems
	- later simplified to make less sub problems and more focused
	- I made some problems like flow charts
	- next time, I'd be more familiar with what the end goal should look like and I would be faster getting a high level decomposition drawn out.
