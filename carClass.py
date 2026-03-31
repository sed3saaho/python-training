#Continuation from classes.py (Importing classes)
#In this module we are going to only write the code from the class Car.

"""A class that can be used to represent a car."""#We included a module-level docstring that briefly describes the contents of this module. You should write a docstring for each module that you are creating.
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.car_make = make
        self.car_model = model
        self.car_year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.car_year} {self.car_make} {self.car_model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reding to the given value.
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

# Storing Multiple Classes in a Module
#You can store as many classes as you need in a single module, although each class in a module should be related somehow. The classes Battery and ElectricCar both help represent cars, so let’s add them to the module carClass.py.(This module)
"""A set of classes used to represent gas and electric cars."""
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.car_make = make
        self.car_model = model
        self.car_year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.car_year} {self.car_make} {self.car_model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reding to the given value.
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
class Battery:
    """A simple attempt to  model a battery for an electric car."""
    def __init__(self, battery_size = 75):
        """Initialize the battery's attributes"""
        self.car_battery_size = battery_size
    def describe_battery(self):
        """Print a statement  describing the battery size"""
        print(f"This car has a {self.car_battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.car_battery_size == 75:
            range = 260
        elif self.car_battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the Parent class
        Then initialize attributes specific to an electric car."""
        super().__init__(make,model,year)
        self.battery = Battery()