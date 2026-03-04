def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()
#learning more about docstrings
print(greet_user.__doc__)#accessing the docstring at runtime
help(greet_user)#using the help fuction to generate the documentation of a given function from the docstring

#Passing Information to a function
def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!!")

greet_user('jesse')
greet_user('elina')

#Positional Argument
def describe_pet (animal_type, pet_name):
    """Display information about the pet."""
    print(f"\nI have a {animal_type.title()}")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
#Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')

#Using Default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a Pet"""
    print(f"\nI have a {animal_type.title()}")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')#Keyword Argument
describe_pet('ruma')#Positional Argument
describe_pet('kitty', 'cat')#Because an explicit argument for animal_type is provided, Python will ignore the parameter’s default value.

#NOTE: When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.

#Equivalent Function Calls
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a Pet"""
    print(f"\nI have a {animal_type.title()}")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
    # A dog named Willie.
    describe_pet('willie')
    describe_pet(pet_name='willie')
    # A hamster named Harry.
    describe_pet('harry', 'hamster')
    describe_pet(pet_name='harry', animal_type='hamster')
    describe_pet(animal_type='hamster', pet_name='harry')

#Return Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name.title()}  {last_name.title()}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(f"Our musician of the day is {musician}")

#Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(f"\n\tOur musician of the day is {musician}")
player = get_formatted_name('bonface', 'otieno', 'ondieki')
print(f"\n\tThe only Fisi here is {player}!!!")

#Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}# in our dictionary the value of first_name is stored in the key 'first' and the value of last_name is stored in the key 'last'
    return person
musician = build_person('jimi' ,'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix', age=27)
print(musician)

#Using a Function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a Full name, neatly formatted"""
    full_name = f"{first_name}, {last_name}"
    return full_name.title()
#This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name (Press q to quit): ")
    if f_name.lower() == 'q':
        break

    l_name = input("Last name (Press q to quit): ")
    if l_name.lower() == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello , {formatted_name}!")

def describe_user(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name
while True:
    name1 = input("Enter your first_name (Press q to exit)")
    if name1.lower() == 'q':
        break
    name2 = input("Enter your last_name(Press q to quit)")
    if name2.lower() == 'q':
        break

    official_name = describe_user(name1, name2)
    print(f"\nHello, {official_name}!\n")

#Passing a List to  a Function
def greet_user(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)
usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)

#Modifying a List in a Function
#The example below is an illustration without using functions
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
#Simulate printing each design, until none are left.
#Move each design to completed models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
#Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_models)

#In our next example we are going to do the same implement the same logic above but with the help of functions..
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
       Move each design to completed_models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#NOTE: This syntax works no matter how many arguments the function recieves.
#Trying with Lists:
def make_pizza(*toppings):
    """Trying to work with List in Arbitrary Arguments."""
    for topping in toppings:
        for name in topping:
            print(f"\n{name.title()}")
names = ['brian', 'loise', 'john']
cars = ['audi', 'rav4', 'harrier']
make_pizza(names)
make_pizza(names, cars)

#Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using Arbitrary Keyword Arguments.
#Sometimes you will want to accept an arbitrary number of keyword arguments, but you won't know ahead of time what kind of information will be passed to the function. in this case, you can write functions that accepts as many key-value pairs as the calling statement provides.
#...One example involves building user profiles: you know you will get information about a user, but you are not sure what kind of information you will receive. The function build_profile() in the following example always takes in a fisrt and last name, but it accepts and arbitrary numebr of keyword arguments as well
def build_profile(first, last, **user_info):
    """Build a dictionary containing everyting we know about a user."""
    user_info['fisrt_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einsten',
                             location= 'princeton',
                             field= 'physics')
print(user_profile)
#The definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want. The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary.  Within the function, you can access the key-value pairs in user_info just as you would for any dictionary.
#In the body of the build_profile, we add  the first and last names to the user_info dictionary because we'll always receive these two pieces of information from the user, and they haven't been placed into the dictionary yet. Then we return the user_info dictionary to the function call line.
#We call build_profile(), passing it the first name 'albert', the last name 'einstein', and the two key-value pairs location='princeton' and field='physics'. We assign the returned profile to user_profile and print user_profile:
##NOTE:You’ll often see the parameter name **kwargs used to collect non-specific keyword arguments.


#Sorting Your Functions into Modules
#One advantage of functions is the way they separate blocks of code from your main program.By using descriptive names for your functions, your main program will be much easier to follow. You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program. An import statement tells Python to make the code in a module available in the currently running program file.
#Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic. It also allows you to reuse functions in many different programs. When you store your functions in separate files, you can share those files with other programmers without having to share your entire program. 
#NOTE: Knowing how to import functions also allows you to use libraries of functions that other programmers have written.
#There are several eays of importing a module and each of these are shown below:

#Importing an Enrire Module.
#To start importing functions, we first need to create a module. A module is a file ending in .py that contains the code you want to import into your program.
#Let's make a module that contains the function make_pizza().To make this module, we will create a file named pizza.py that will only contain the function make_pizza():
