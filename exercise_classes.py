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
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't inclde a negative value")


my_used_car = Car('subaru', 'outback', 2015) 
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#Exercises...
class Restaurant:
    """Modelling an example of a Restaurant"""
    def __init__(self, name, type):
        """Initialize attributes to make a Restaurant"""
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        """Printing the two pieces of information of the restaurnat"""
        restaurant_details = f" The Reasturant name is {self.restaurant_name.title()} and cuisine type is {self.cuisine_type.title()}"
        return restaurant_details
    def open_restaurant(self, status):
        """Show whether the restaurant is open or closed"""
        if status == 'open':
            print("The restaurant is opened")
        elif status == 'close':
            print("The restaurant is closed")
restaurant_from_class = Restaurant('fogo gaucho', 'brazilian')
print(f"{restaurant_from_class.restaurant_name.title()}")
print(f"{restaurant_from_class.cuisine_type.title()}")
# NOTE:Since describe_restaurant() now RETURNS a value, you must PRINT the call:
print(restaurant_from_class.describe_restaurant())
restaurant_from_class.open_restaurant('open')

restaurant_1 = Restaurant('carnovire', 'italian')
print(restaurant_1.describe_restaurant())
restaurant_2 = Restaurant('massai mara', 'massai')
print(restaurant_2.describe_restaurant())


class User:
    """Modelling a class to represent a user"""
    def __init__(self, name1, name2):
        """Initialize attributes for the user"""
        self.first_name = name1
        self.last_name = name2
        self.age = 1
        self.gender = 'male'
    def describe_user(self, gender, age):
        """Print summary of the user's information"""
        self.gender = gender
        self.age = age
        print(f"First Name: {self.first_name.title()}")
        print(f"Last_name: {self.last_name.title()}")
        print(f"Gender {self.gender.title()}")
        print(f"Age: {self.age}")
    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!!!")

user_1 = User('stephen', 'otieno')
user_1.describe_user('male', 23)
user_1.greet_user()

user_2 = User('bradly', 'omondi')
user_2.describe_user('male', 15)
user_2.greet_user()

user_3 = User('stephanie', 'ochieng')
user_3.describe_user('female', 27)
user_3.greet_user()

#Revised versionof the User class
class User:
    """Modelling a class to represent a user"""
    
    def __init__(self, first, last, age, gender):
        """Initialize attributes for the user immediately"""
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Print summary of the user's information"""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Gender: {self.gender.title()}")
        print(f"Age: {self.age}")

    def greet_user(self):
        """Print a personalized greeting"""
        print(f"Hello, {self.first_name.title()}! Welcome back.")

# Creating instances with all data upfront
user_1 = User('stephen', 'otieno', 23, 'male')
user_2 = User('bradly', 'omondi', 15, 'male')
user_3 = User('stephanie', 'ochieng', 27, 'female')

# Calling methods
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

#Adding more logic on the previous exercise
class Restaurant:
    """Modelling an example of a Restaurant"""
    def __init__(self, name, type):
        """Initialize attributes to make a Restaurant"""
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
    def describe_restaurant(self):
        """Printing the two pieces of information of the restaurnat"""
        restaurant_details = f" The Reasturant name is {self.restaurant_name.title()} and cuisine type is {self.cuisine_type.title()}"
        return restaurant_details
    def open_restaurant(self, status):
        """Show whether the restaurant is open or closed"""
        if status == 'open':
            print("The restaurant is opened")
        elif status == 'close':
            print("The restaurant is closed")
    def set_number_served(self, value):
        """Update the value of attribute self.number_served"""
        if value > 0:
            self.number_served = value
        else:
            print("You can't include a negative value")
    def increment_number_served(self, increment_value):
        if increment_value > 0:
            self.number_served += increment_value
        else:
            "No negative Values"

restaurant = Restaurant('fogo gaucho', 'brazilian')
print(f"The total number of customers served today are {restaurant.number_served}")
restaurant.number_served = 258
print(f"The total number of customers served today are {restaurant.number_served}")
restaurant.set_number_served(173)
print(f"The total number of customers served today are {restaurant.number_served}")
restaurant.increment_number_served(20)
print(f"The total number of customers served today are {restaurant.number_served}")


class User:
    """Modelling a class to represent a user"""
    
    def __init__(self, first, last, age, gender):
        """Initialize attributes for the user immediately"""
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Print summary of the user's information"""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Gender: {self.gender.title()}")
        print(f"Age: {self.age}")

    def greet_user(self):
        """Print a personalized greeting"""
        print(f"Hello, {self.first_name.title()}! Welcome back.")
    
    def increment_login_attempts(self):
        """Increase the login attempt by one"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the value of the login_attempts to 0"""
        self.login_attempts = 0
user1 = User('Brad', 'otieno', 13, 'male')
user1.increment_login_attempts()#1st call
print(f"You attempted to login {user1.login_attempts} times")
user1.increment_login_attempts()#2nd call
user1.increment_login_attempts()#3rd call
print(f"You attempted to login {user1.login_attempts} times")
user1.increment_login_attempts()#4th call
print(f"You attempted to login {user1.login_attempts} times")

#Reset
user1.reset_login_attempts()
print(f"You attempted to login {user1.login_attempts} times")
#Done on Exercises
#dsdsfere

#Inheritance
class Car:
    """A simple attempt to represent a car."""
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
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't inclde a negative value")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

#Defining Attributes and Methods for the Child Class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the Parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#Overriding Methods from the Parent Class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the Parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):#Example method , if it were also in the Car class
        """Electric Cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2019)



