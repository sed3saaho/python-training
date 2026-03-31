#Now we make a separate file called mycarClass.py. This file will import the Car class from carClass.py and then create an instance from that class:
from carClass import Car#The import statement here tells Python to open the carClass module and import the class Car.

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#Now we can use the Car class as if it were defined in this file
