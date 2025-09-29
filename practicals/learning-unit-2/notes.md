# Object oriented programming

```python
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Colour: {self.colour}, Speed: {self.speed} km/h")


# Creating instances of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# Accessing and modifying object attributes
car1.accelerate(20)
car2.accelerate(30)
car1.brake(5)

# Displaying car information
car1.display_info()
car2.display_info()
```

In this example, we define a `Car` class with attributes like brand, model, colour, and speed. The class also has methods to accelerate, brake, and display information about the car. We then create two instances of the `Car` class (`car1` and `car2`) and perform operations on them, such as accelerating, braking, and displaying their information.

Please note that this is a simplified example to demonstrate the concept of object-oriented programming in Python. In real-world scenarios, classes and objects can have more attributes and methods based on the requirements of the application.