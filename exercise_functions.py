def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()
#learning more about docstrings
print(greet_user._doc_)#accessing the docstring at runtime
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
