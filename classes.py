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
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't inclde a negative value")

my_used_car = Car('subaru', 'outback', 2015)#We create a  used car, my_used_car
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)#We set its odometer to 23,500 by calling update_odometer() and passing it 23_500
my_used_car.read_odometer()

my_used_car.increment_odometer(100)#We call increment_odometer() and pass it 100 to add the 100 miles that we drove between buying the car and registering it:
my_used_car.read_odometer()
#You can easily modify the increment_odometer_method to reject negative increments so no one uses this function to roll back an odometer.

#Inheritance
#You don't always have to start from scratch when writing a class. If the class you are writing is a specialized version of another class  you wrote, you can use inheritance.
#When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent class, and the new class is called the child class. 
#The child class can inherit any or all of the attributes of it's  parent class, but it's also free to define new attributes and methods of it's own.

##The __init__() Method for a Child Class
#When you are writing a new class based on an existing class, you will often want to call the __init__() method from the parent class. This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class.
#As an example, let's model an electric car. An electric car is just a specific kind of car, so we can base our new ElectricCar class on the Car Class we wrote earlier. Then we will only have to write code for the attributes and behavior specific to electric cars.

#Let’s start by making a simple version of the ElectricCar class, which does everything the Car class does:
class Car:#NOTE:NOTE: We start with Car. When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.
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

class ElectricCar(Car):#NOTE: NOTE: We define the child class, ElectricCar. The name of the parent class must be included in the parentheses in the definition of a child class.
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):#The __init__() method here takes in the information required to make a Car instance
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)#NOTE: The super() function here is a special function that allows you to call a method from the parent class. This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method.
        ##NOTE: The name super comes from a convention of calling the parent class a superclass and the child class a subclass.
my_tesla = ElectricCar('tesla', 'model s', 2019)#we make an instance of the ElecticCar class and assign it to my_tesla. This line calls the __init__() method defined in ElectricCar, which in turn tells Python to call the __init__() method defined in the parent class Car. We provide the arguments 'tesla', 'model s' and 2019.
#Aside from __init__(), there are no attributes or methods yet that are particular to an electric car. At this point we are just making sure the electric car has the appropriate Car behaviors:
print(my_tesla.get_descriptive_name())

#Defining Attributes and Methods for the Child Class
#Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.
#Let’s add an attribute that’s specific to electric cars (a battery, for example) and a method to report on this attribute. We’ll store the battery size and write a method that prints a description of the battery:
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the Parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)##NOTE:NOTE: Notice that when calling super().__init__(), you do not include self in the parentheses. Python handles self automatically when you use super().
        self.battery_size = 75 #NOTE: We add a new attribute self.battery_size and set it's initial value to say, 75. This attribute will be associated with all the instances created from the ElectricCar class but won't be associated with any instance of Car.
    
    def describe_battery(self):#We also add a method called describe_battery() that prints information about the battery. When we call this method, we get the description that is clearly specific to an electric Car:
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

##NOTE: NOTE:here’s no limit to how much you can specialize the ElectricCar class. You can add as many attributes and methods as you need to model an electric car to whatever degree of accuracy you need. An attribute or method that could belong to any car, rather than one that’s specific to an electric car, should be added to the Car class instead of the ElectricCar class. Then anyone who uses the Car class will have that functionality available as well,
##.....NOTE:and the ElectricCar class will only contain code for the information and behavior specific to electric vehicles.

#Overriding Methods from the Parent Class
#You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class.
#..To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.
#Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, so you might want to override this method. Here’s one way to do that:
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
    def fill_gas_tank(self):
        """Electric Cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2019)
#Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car and run this code instead. When you use inheritance, you can make your child classes retain what you need
#.....and override anything you don’t need from the parent class.

#Intsances as Attributes
#When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. You’ll find that you have a growing list of attributes and methods and that your files are becoming
#..lengthy. In these situations, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together.
#For example, if we continue adding detail to the ElectricCar class, we might notice that we’re adding many attributes and methods specific to the car’s battery. When we see this happening, we can stop and move those
#...attributes and methods to a separate class called Battery. Then we can use a Battery instance as an attribute in the ElectricCar class:
class Battery:#We define a new class Battery that doesn't inherit from any other class
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):#The __init__() method here has one parameter, battery_size, in addition to self. This is an optional parameter that sets the battery's size to 75 of no value is provided.
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
    def describe_battery(self):#The method describe battery has been moved to this class as well.
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the Parent class.
        Then initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
#In the ElectricCar class, we now add an attribute called self.battery. The line below tells Python to create a new instance of Battery(with a default size of 75, because we're not specifying value) and assign that instance to the attribute self.battery. This will  happen every time the __init__() method is called' any ElectricCar instance will now have a Battery instance created automatically
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)#We create an electric car and assign it to the variable my_tesla. When we want to describe the battery, we need to work through the car’s battery attribute:
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()#This line tells Python to look at the instance my_tesla, find it's battery attribute, and call the method describe_battery() that's associated with the Battery instance stored in the attribute.
#NOTE:This looks like a lot of extra work, but now we can describe the battery in as much detail as we want without cluttering the ElectricCar class. Let’s add another method to Battery that reports the range of the car based on the battery size:
class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on full charge")
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the Parent class.
        Then initialize attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#NOTE:NOTE:BONUS TIP
#Some of the things to note while working with classes and instances is how texts are highlighted
#If the instance you created is connected to an attribute from the class then the whole text will be in blue as shown below
my_tesla.odometer_reading = 24
#And if the instance you created is trying to connect or is connected to a method in the class , then the method from the class will be in colour yellow, while the name of the instance will be in blue.
my_tesla.read_odometer()


#Imporing Classes
#Let’s create a module containing just the Car class. This brings up a subtle naming issue:
#Refer to carClass.py and my_carClass.py for further illustrations.
#Importing classes is an effective way to program. Picture how long this program file would be if the entire Car class were included. When you instead move the class to a module and import the module, you still get all the same functionality, but you keep your main program file clean and easy
#.....to read. You also store most of the logic in separate files; once your classes work as you want them to, you can leave those files alone and focus on the higher-level logic of your main program

#Storing Multiple Classes in a Module
#You can store as many classes as you need in a single module, although each class in a module should be related somehow. The classes Battery and ElectricCar both help represent cars, so let’s add them to the module carClass.py

#Importing Multiple Classes from a Module
#You can import as many classes as you need into a program file. If we want to make a regular car and an electric car in the same file, we need to import both classes, Car and ElectricCar: (Refer to my_elctric_car.py)

#Importing an entire module( Refer to my_electric_car.py)
#You can also import an entire module and then access the classes you need using dot notation. This approach is simple and results in code that is easy to read. Because every call that creates an instance of a class includes the module name, you won’t have naming conflicts with any names used in the current file.


#Importing All Classes from a Module
#You can import every class from a module using the following syntax: 
#.....from module_name import *
#NOTE:NOTE:This method is not recommended for two reasons. First, it’s helpful to be able to read the import statements at the top of a file and get a clear sense of which classes a program uses. With this approach it’s unclear which classes you’re using from the module. This approach can also lead to confusion with names in the file. If you accidentally import a class with the same name as something else in your program file, you can create errors that are hard
#..to diagnose. I show this here because even though it’s not a recommended approach, you’re likely to see it in other people’s code at some point. If you need to import many classes from a module, you’re better off importing the entire module and using the module_name.ClassName syntax. You won’t see all the classes used at the top of the file, but you’ll see clearly where the module is used in the program. You’ll also avoid the potential naming conflicts that can arise when you import every class in a module.


#Importing a Module into a Module(Page 216/ 178)
#Sometimes you’ll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module. When you store your classes in several modules, you may find that a class in one module depends on a class in another module. When this happens, you can import the required class into the first module.
#For example, let’s store the Car class in one module and the ElectricCar and Battery classes in a separate module. We’ll make a new module called electric_car.py—replacing the electric_car.py file we created earlier—and copy just the Battery and ElectricCar classes into this file
#The class ElectricCar needs access to its parent class Car, so we import Car directly into the module at u. If we forget this line, Python will raise an error when we try to import the electric_car module. We also need to update the Car module so it contains only the Car class:


#Using Aliases
#As you saw in Chapter 8, aliases can be quite helpful when using modules to organize your projects’ code. You can use aliases when importing classes as well. As an example, consider a program where you want to make a bunch of electric cars. It might get tedious to type (and read) ElectricCar over and over again. You can give ElectricCar an alias in the import statement:
from carClass import ElectricCar as EC
#Now you can use this alias whenever you want to make an electric car:
my_tesla = EC('tesla', 'roadster', 2019)