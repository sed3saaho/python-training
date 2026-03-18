#Creating and Using a Class
class Dog:#
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initalize name and age attributes"""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")
#Making an Instance from a Class
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
#Accessing Attributes
my_dog.name
print(f"{my_dog.name}")
#Calling methds
my_dog = Dog('Willie', 6)#Creating the instance
my_dog.sit()
my_dog.roll_over()

class Dog:
    """A simple attemot to model a Dog"""
    def __init__(self, name, age):
        """Initalize name and age attributes"""
        self.dog_name = name
        self.dog_age = age
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.dog_name} is now sitting")
    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.dog_name} is rolling over")
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.dog_name}.")
print(f"My dog is {my_dog.dog_age} years old")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.dog_name}.")
print(f"You dog is {your_dog.dog_age} years old.")
your_dog.sit()
your_dog.roll_over()

#Working with Classes and Instances
class Car:
    """A simple attemt to describe a car ."""
    def __init__(self, make, model, year):
        self.car_make = make
        self.car_model = model
        self.car_year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.car_year} {self.car_make} {self.car_model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

#Setting a Default Value for an Attribute
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.car_make = make
        self.car_model = model
        self.car_year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
         """Return a neatly formatted descriptive name."""
         long_name = f"{self.car_year} {self.car_make} {self.car_model}"
         return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# 1.Modifying an Attribute's Value Directly
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23#We set the odometer reading to 23 directly:
my_new_car.read_odometer()
#2. Modifying Attribute's Value through a Method:
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.car_make = make
        self.car_model = model
        self.car_year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
         """Return a neatly formatted descriptive name."""
         long_name = f"{self.car_year} {self.car_make} {self.car_model}"
         return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    #The method below update_odometer() takes in mileage value and assigns it to self.odometer_reading.
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        self.odometer_reading = mileage
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)#We call update_odometer() and give it 23 as an argument
my_new_car.read_odometer()
#Improving the efficiency of the update_odometer() method:
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.car_make = make
        self.car_model = model
        self.car_year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
         """Return a neatly formatted descriptive name."""
         long_name = f"{self.car_year} {self.car_make} {self.car_model}"
         return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    #Improving the efficiency of the update_odometer() method:
    def update_odometer(self, mileage):
        """Set the odometer reading to the given Value. Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

#Incrementing an Attribute's Value Through a Method:
class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.car_make = make
        self.car_model = model
        self.car_year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
         """Return a neatly formatted descriptive name."""
         long_name = f"{self.car_year} {self.car_make} {self.car_model}"
         return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given Value. Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015) 
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


