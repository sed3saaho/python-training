#in this file we are going to import the ElectricCar class, and make an electric car:
from carClass import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#You can import as many classes as you need into a program file. If we want to make a regular car and an electric car in the same file, we need to import both classes, Car and ElectricCar:
from carClass import Car, ElectricCar#You import multiple classes from a module by separating each class with a comma

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
#Once you’ve imported the necessary classes, you’re free to make as many instances of each class as you need.



#Importing an entire module
#You can also import an entire module and then access the classes you need using dot notation. This approach is simple and results in code that is easy to read. Because every call that creates an instance of a class includes the module name, you won’t have naming conflicts with any names used in the current file.
#Below is how it looks like to import the entire car module and ten create a regular car and an electric car:
import carClass#we import the entire carClass module.

my_beetle = carClass.Car('volkswagen', 'beetle', 2019)##NOTE: We then access the classes we need through the module_name.ClassName syntax
print(my_tesla.get_descriptive_name())