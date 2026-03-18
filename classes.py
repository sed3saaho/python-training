#In object oriented programming you write classes that represent real world things and situations, and you create objects based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.
#When you create individual objetcs from the class, each objects is automatically equipped with the general behavior; you can then give each oject whatever unique traits you desire.
#Making an Object from a class is called instantiation, and you work with instances of a class. In this chapter you will write classes and create instances of those classes. You will specify the kind of information that can be stored in instances, and you will define actions that can be taken with these instances>
#You will also write classes that extend the functionality of of existing classes, so similar classes can share code efficiently. You will store your classes in modules and import classes written by other Programmers into your own program files

#Creating and Using a Class
#You can model almost anything using classes. Let's start by writing a simple class, Dog, that represents a dog--not one dog in particular, but any dog.
#What do we know about most pet dogs? Well, they all have a name and age. We also know that most dogs sit and roll over. Those two pieces of information (name and age) and those two behaviors (Sit and roll over) will go in our dog class, because they are common to most dogs.
#This class will tell Python how to make an object representing a dog. After our class is written, we'll use it to make individual instances, each of which represents one specific dog.
#NOTE:Each instances created from the Dog class will store a name and age, and will give each dog the ability to sit() and roll_over():
class Dog:#We define a class named Dog. By convention, capitalized names refer to classes in Python. NOTE:There are no parenthesis in the class definition because we are creating this class from scartch.
    """A simple attempt to model a dog"""#We write a docstring describing what this class does
#A function that's part of a class is a method. Everything you learned about functions applies to methods as well; the only practical difference for now is the way we will call methods
    def __init__(self, name, age):#NOTE:The __init__() is a special method that Python runs automatically whenever we create a new instance based on the Dog class. NOTE: This method has two leading underscores and two trailing underscores, a convention that helps prevent Python's default method names from conflicting with your method names. if you use just one underscore ach side, the method won't be called automatically when you use your class, which can result in errors that are difficult to identify.
#We define the __init__() method to have three parameters: self, name, and age. The self parameter is required in the method definition, and it must come first before the other parameters. It must be included in the definition because when Python calls this method later( to create  an instance of Dog) the method call will automatically pass the self argument.Every method call associated with an instance automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.
#When we make an instance of Dog, Python we call the __init__() method from the Dog class. We will pass Dog() a name and an age as arguments; self is passed automatically, so we don't need to pass it. Whenever we want to make an instance from the Dog class, we will provide values for only the last two parameters, name and age.
        """Initalize name and age attributes"""
#The two variables defined below, each have the prefix self. Any variable prefixed with self is available to every method in the class, and we will also be able to access these variables  through any instance created from the class. The line self.name = name takes the value associated with the parameter name and assigns it to the variable name, which is then attached to the instance being created. The same process happens with self.age = age. 
# #Variables that are accessible through instances like this are called attributes.
        self.name = name
        self.age = age
#The Dog class has two other methods defined: sit() and roll_over(). Because these two methods don't need additional information to run, we just define them to have one parameter, self. The instances we create later will have access to these methods. In other words they will be able to sit and roll_over(). For now sit and roll_over don't do much but just print a simpl message saying the dog is sitting or rolling over..... but in animated program we could design these instances to show an animation of a dog sitting or rolling.
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")
    
#Making an Instance from a Class
#Think of a class as a set of instructions for how to make an instance. The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs.
#Let's  make an instance representing a specific dog:
my_dog = Dog('Willie', 6)#Here we tell Python to create a dog whose name is  'Willie' and whose age is 6. When Python reads this line, it calls the __init__ method in Dog with the arguments 'Willie' and 6.
#The __init__() method creates an instance representing this particular dog and sets the name and age attributes using th values we provided.Python then returns an instance representing this actual dog.NOTE:We assign that instance to the variable my_dog.
#The naming convention is helpful here: we can usually assume that a capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#Accessing Attributes
#To access the attributes of an instance, you use dot notation. In our example above we access the value of my_dog's attribute name by writing:
my_dog.name
#Here Python looks at the instance my_dog and then finds the attribute name associated with my_dog. This is the same attribute reffered to as self.name in the class Dog

#Calling Methods
#After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog. Let's make our dog sit and roll over:
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
#To call a method, give th name of the instance (in this case, my_dog) and the method you want to call, separated by a dot. When Python reads my_dog.sit() it looks for the method sit() in the class Dog and runs that code. same case for the line my_dog.roll_over()
#NOTE: This syntax is quite useful. When attributes and methods have been given descrptive names like name, age, sit(), and roll_over(), we can easily infer what a block of code, even one we have never seen before is supposed to do.

#Creating Multiple instances
#You can create as many instances from a class as you need. Let's create a  second dog called your_dog
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
#In the above example we create a dog named Willie and a dog named Lucy. Each Dog is a separate instance with it's own set of attributes, capable of the same set of actions:
#Even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class. You can make as many instances from one  class as you need , as long as you give each instance a unique variabke name or it occupies a unique spot in a list or a dictionary.


#Working with Classes and Instances
#You can use classes to represent real world situations. Once you write a class you will spend most of your time working with instances created from that class. One of the first tasks you will want to do is to modify the attributes associated with a particular instance.
#......You can modify the attributes of instance directly or write methods that update the attributes in specific ways.

#In our next example we are going to define a Car class, which is going to store information about the kind of car we are working with, and it will have a method that summarizes this information:
class Car:
    """A simple attemt to describe a car ."""
    def __init__(self, make, model, year):#The __init__ method takes in the parameters 'make' 'model' and 'year' and assigns them to the attributes that will be associated with instances made from this class. When we make a new car instance, we will need tp specify a make, model, and year for our instance.
        self.car_make = make
        self.car_model = model
        self.car_year = year
    def get_descriptive_name(self):#This method puts a car's year, make, and model into one string neatly describing the car.
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.car_year} {self.car_make} {self.car_model}"#To work with the attribute values in this method, we use self.car_make, self.car_model, and self.car_year
        return long_name.title()#NOTE: NOTE: Since you are returning  a value, you will have to print the function hen you will be calling it later on

my_new_car = Car('audi', 'a4', 2019)#We make an instance from the Car class and assign it to the variable my_new_car.
#NOTE:NOTE: Since get_desriptive_name() RETURNS  a value you must PRINT the call:
print(my_new_car.get_descriptive_name())#Then we call get_descriptive_name() to show what kind of car we have.

#NOTE: To make a class more interesting , let's add an attribute that changes over time. We will add an attribute that stores the car's overall mileage.

#Setting a Default Value for an Attribute
#When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the __init__ method, where they are assigned a default value.
#Let's add an attribute called odometer_reading that always starts with a value of 0. We will also add a method read_odometer() that helps us read each car's odometer:

class Car:
    def __init__(self, make, model, year):#This time when Python calls the __init__() method to create a new instance, it stores the make, model, and year value as attributes like it did in the previous example.
        """Initialize attributes to describe a car."""
        self.car_make = make
        self.car_model = model
        self.car_year = year
        self.odometer_reading = 0#Then Python creates a  new attribute called odometer_reading and sets its intial value to 0
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

#Modifying Attribute Values
#You can change an attribute's value in three ways: you can change the value directly through an isntance, set the value through a method, or increment the value (add a certain amount to it) through a method. Let's look at each of these approaches.
# 1.Modifying an Attribute's Value Directly
#The simplest way to modify the value of an attribute is to access the attribute directly through an instance. below we will set the odometer reading to 23
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23#We use dot notation to access the car's odometer_reading attribute and set its value directly. This line tells Python to take the instance my_new_car, find the attribute odometer_reading associated with it, and set the value of that attribute to 23
my_new_car.read_odometer()

# 2.Modifying an attribute's Value through a Method
#It can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally. Below is an example showing a method called update_odometer():
class Car:
    def __init__(self, make, model, year):#This time when Python calls the __init__() method to create a new instance, it stores the make, model, and year value as attributes like it did in the previous example.
        """Initialize attributes to describe a car."""
        self.car_make = make
        self.car_model = model
        self.car_year = year
        self.odometer_reading = 0#Then Python creates a  new attribute called odometer_reading and sets its intial value to 0
    def get_descriptive_name(self):
         """Return a neatly formatted descriptive name."""
         long_name = f"{self.car_year} {self.car_make} {self.car_model}"
         return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    #The only modification to Car is the addition of the method below update_odometer()
    def update_odometer(self, mileage):#This method takes in a mileage value and assigns it to self.odometer_reading.
        """Set the odometer reading to the given value"""
        self.odometer_reading = mileage
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)#We call  update_odometer() and give it 23 as an argument (corresponding to the mileage parameter in the method definition)
my_new_car.read_odometer()

#We can extend the method update_odometer() to do additional work every time the odometer reading is modified. Lets add a little logic to make sure no one tries to roll back the odometer reading
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
    #Improving the efficiency of the update_odometer() method
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
#Now the update_odometer() method checks that the new reading makes sense before modifying the attribute. if the new mileage is greate than or equal to the existing mileage, self.odometer_reading, you can update the odometer reading to the new mileage. and if the new mileage is less than the existing mileage, you will get a warning that you can't roll back the odometer.


#Incrementing an Attribute's Value Through a Method
#Sometimes you will want to increment an attribute's value by a certain amount rather than set an entirely new value. Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it. We will define a method below that allows us to pass this incremental amount and add that value to the odometer reading:
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
    #Improving the efficiency of the update_odometer() method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given Value. Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    #The new method increment_odometer() takes in a number of miles and adds this value to self.odometer_reading.
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015)#We create a  used car, my_used_car
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)#We set its odometer to 23,500 by calling update_odometer() and passing it 23_500
my_used_car.read_odometer()

my_used_car.increment_odometer(100)#We call increment_odometer() and pass it 100 to add the 100 miles that we drove between buying the car and registering it:
my_used_car.read_odometer()
#You can easily modify the increment_odometer_method to reject negative increments so no one uses this function to roll back an odometer.