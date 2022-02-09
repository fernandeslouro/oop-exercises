#%% OOP Exercise 1: Create a Class with instance attributes: Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

ford_focus = Vehicle(250, 7.8)
print(ford_focus.max_speed, ford_focus.mileage)


# %% OOP Exercise 2: Create a Vehicle class without any variables and methods

# Eu tinha criado uma classe init com o "pass", penso que iria dar ao mesmo
class Vehicle():
    pass

# %% OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class 

# Given
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 130, 20)


print(school_bus.name, school_bus.max_speed, school_bus.mileage)

# %% OOP Exercise 4: Class Inheritance: Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Given
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# My Solution
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=50):
        super(Bus, self).__init__(name, max_speed, mileage)
        self.capacity = capacity
    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"

vbus = Bus("Buzi", 120, 20)
vbus.seating_capacity()

# Their solution
class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())

# %% OOP Exercise 5: Define a property that must have the same value for every class instance (object): Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle:
    # Added just this line
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass