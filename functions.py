#A Function is a named block of code designed to do one specific job. When you want to perform a particular task that you have defined in a function, you call the function responsible for it.
#You will learn to store functions in separate files called modules to help  organize your main program files.
#Definig a Function
#Note that while defing a function we will have to use the def keyword, and also name the function followed by a set of parantheses then a colon then the block of code inside the function
def greet_user():#we use the keyword def to tell Python that we are defining a function, which tells Python the name of the function , and if appliclable what kind of information the function needs to do it's job. The parentheses hold that information. in our case the function name is greet_user and it needs no information to do its job so it's parenthesis are empty.
    #Any indeneted line  that follows the def greet_user(): make up the body of the function.
    """Display a simple greeting"""#This text is a comment called docstring , which describes what the fuction does. Docstring are enclosed in triple quotes which Python looks for when it generates documentation for the fuctions in your programs. and they are normally placed at the begining of a module eg a function or a class
    #The difference between a docstring and a regular comment is that the docstrings are accessible during runtime via the _doc_ attribute, which makes them useful for introspection and generating documentation automatically.......comments are ignored at runtime, Docstrings are stored in _doc_ and can be accessed programmatically,,,,Function like help use docstrings to display useful information
    print("Hello!")

greet_user()#When you want to use a fucntion you call it.To call a fucntion you write the name of the function followed by any necessary information in Parentheses. and because no information is needed here, calling our function is as simple as entering greet_user() and as expected, it prints Hello!
#Learning more about docstrings
print(greet_user.__doc__)#accessing the docstring at runtime.....NOTE: note that the underscores are two on both sides.
help(greet_user)#using the help fuction to generate the documentation of a given function from the docstring


#Passing informtion to a Function
#We wiil modify our previous function so as to include the name of the user while greeting them
#For the function to greet the user by name, you enter username or name or name1........ in the parenthesis of the function's definition at def greet_user(). By adding username here you allow the function to accept any value of username you specify.
#.........The function will now expect you to provide a value for username each time you call it. When you call greet_user(), you can pass it a name, such as 'jesse' inside the parantheses:
def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!!") 

greet_user('jesse')#This Calls greet_user(username) function and gives the function the information it needs to execute the print() call
greet_user('elina')

#Arguments and Parameters
#In our previous example the variable username in the definition greet_user() is an example of a parameter, a piece of information the function needs to do it's job. The value like 'jesse' in greet_user('jesse) is an example of an Argument.
#An argument is a piece pf information that is passed from a function call to a function. When we call a function, we place the value we want the function to work with in parenthesis. in our case the argument 'jesse' was passed to the function greet_user() and the value was assigned to the parameter username
#Passing Arguments
#Because a function can have multiple parameters, a function call may need multiple arguments. You  can pass arguments to your functions in a number of ways:
#You can use positional arguments, which need to be in the same order the parameters were written; keyword arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values
#In positional argument when you call a function, Python must match each argument in the function call with a parameter in the function definition. the simplest way to do this is based on the order of the arguments provided. value matched up this way are called posistional arguments:
def describe_pet (animal_type, pet_name):#Definition has two parameters that shows this function needs a type of animal and the animal's name
    """Display information about the pet."""
    print(f"\nI have a {animal_type.title()}")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')#In the function call the argument 'hamster' is assigned to the parameter animal type and the argument 'harry' is assigned to the parameter pet_name
describe_pet('dog', 'willie') #Multiple function calls  page 132 or 168
#NOTE: You can use as many positional arguments as you need in your functions .Python works through the arguments you provide when calling the function and matches each one with the corresponding parameter in the function’s definition.
#NOTE: Order Matters in Positional Arguments cause You can get unexpected results if you mix up the order of the arguments in a function call when using positional arguments:
describe_pet('harry', 'hamster')#This will give us a wrong output based on the function we defined above

#Keyword Arguments
#A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when  you pass the argument to the function there will be no confusion as in the positional argument. because they clarify the role of each value in the function call.
def describe_pet(animal_type, pet_name):#The function describe pet hasn't changed. But when we call the function, we explicitly tell Python which parameters each argument should be matched with
    """Display information about pet"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')#The order of heyword argumets doesn't matter because Python knows where each value should go.
#The following two functions below are equivalent: Because order doesn't matter
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

#Default Values
#When wriring a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter's default value. So when you define a default value for a parameter you can exclude the corresponding argument you'd usually write in the function call.
#For example in our describe_pet function we can decide to set the defaulr value for animal_type as dog if we notice most of our user's animal type is a dog. Now anyone calling describe_pet() for a dog can omit that information:
def describe_pet(pet_name, animal_type='dog'):#We changed the definition of describe_pet() to include a default value, dog', for animal_type. Now when the function is called with no animal_type specified, Python knows to use the value 'dog' for this parameter:
    """Display information about a Pet"""
    print(f"\nI have a {animal_type.title()}")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')#Keyword Argument
describe_pet('ruma')#Positional Argument
describe_pet('kitty', 'cat')
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
#Each of these function calls would have the same output as the previous examples. It doesn’t really matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand.

#Avoiding Argument Errors( page 136 or 174)
#When you start to use functions, don’t be surprised if you encounter errors about unmatched arguments. Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work. 

#Return Value
#A function doesn’t always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function. Return values allow you to move much of your program’s grunt work into functions, which can simplify the body of your program.
#Returning a Simple Value
#Let’s look at a function that takes a first and last name, and returns a neatly formatted full name:
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name.title()}, {last_name.title()}"
    return full_name.title()#We return the value after the first name and the last name are assigned to the variable full_name

musician = get_formatted_name('jimi', 'hendrix')
print(f"Our musician of the day is {musician}")
#NOTE: When you call a function that returns a value, you need to provide a variable that the return value can be assigned to. In this case, the returned value is assigned to the variable musician at x. The output shows a neatly formatted name made up of the parts of a person’s name:

#Making an Argument Optional
#Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. You can use default values to make an argument optional.
#For example in our function we would include a parameter for middle name and then make the argument for middle name optional to our users, cause some users might not have a middle name
#To make the middle name optional, we can give the middle_name argument an empty default value and ignore the argument unless the user provides a value. To make get_formatted_name() work without a middle name, we set the
#......default value of middle_name to an empty string and move it to the end of the list of parameters:
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:#we check to see if a middle name has been provided. NOTE: Python interprets non-empty strings as True, so if middle_name evaluates to True if a middle name argument is in the function call . If a middle name is provided, the first, middle, and last names are combined to form a full name. 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:#If no middle name is provided, the empty string fails the if test and the else block runs w. The full name is made with just a first and last name, and the formatted name is returned to the calling line where it’s assigned to musician and printed.
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(f"\n\tOur musician of the day is {musician}")
player = get_formatted_name('bonface', 'otieno', 'ondieki')
print(f"\n\tThe only Fisi here is {player}!!!")
#In this example, the name is built from three possible parts. Because there’s always a first and last name, these parameters are listed first in the function’s definition. The middle name is optional, so it’s listed last in the definition, and its default value is an empty string
#NOTE: NOTE: NOTE: Calling this function with a first and last name is straightforward. If we’re using a middle name, however, we have to make sure the middle name is the last argument passed so Python will match up the positional arguments correctly .
#Optional values allow functions to handle a wide  range of use cases while letting functions calls remain as simple as possible.

#Returning a Dictionary
#A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries. For example, the following function takes in parts of a name and returns a dictionary representing a person:
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}# in our dictionary the value of first_name is stored in the key 'first' and the value of last_name is stored in the key 'last'
    return person#we return the entire dictionary as the return value of our function def build_person()
musician = build_person('jimi' ,'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):#We add a new optional parameter age to the function definition and assign the parameter the special value None, which is used when a variable has no specific value assigned to it. You can think of None as a placeholder value. In conditional tests, None evaluates to False.
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix', age=27)#If the function call includes a value for age, that value is stored in the dictionary. This function always stores a person’s name, but it can also be modified to store any other information you want about a person.
print(musician)

#Using a Function with a while loop
#You can use Python with all the Python structures you have learned abot so far
#For example, let’s use the get_formatted_name() function with a while loop to greet users more formally
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
#For the example above p asks the user to enter their name, and we prompt for their first and last name separately But there’s one problem with this while loop: We haven’t defined a quit condition.
#Where do you put a quit condition when you ask for a series of inputs? We want the user to be able to quit as easily as possible, so each prompt should offer a way to quit. The break statement offers a straightforward way to exit the loop at either prompt:
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print(("enter 'q' at any time to quit"))
    f_name = input("First_name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = (f_name, l_name)
    print(f"\nHello, {formatted_name}!")

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

#Passing a List
#When you pass a list to a function, the function gets direct access to the contents of the list... Let's use functions to make working with lists more efficient.
#........Say we have a list of users and want to print a greeting to each. The example below sends a list of names to a function called greet_users() which greets each person in the list individually:
def greet_user(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)
usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)

#Modifying a List in a Function
#When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function's body are permanent, allowing you to work efficiently even when you are dealing with large amounts of data.
#Consider a company that creates 3D printed models of designs that users submit. Designs that need to be printed are stored in a list, and after being printed they’re moved to a separate list. The following code does this without using functions:
#We start with some designs that need to be printed.
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
    print(completed_model)
#Our program above starts with a list of designs that need to be printed and an empty list called completed_models, that each design will be moved after it has been printed.
#We can reorganize this code by writing two functions, each of which does one specific job.... Most of the code won;t change; we are just making it more carefully structured.. The first function will handle printing the designs and the second will summarize the prints that have been made:
def print_models(unprinted_designs, completed_models):#we define our function with two parameters ; a list of designs that need to be printed and a list of completed models,
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
print_models(unprinted_designs, completed_models)#We call print_models and pass it the two lists it needs;as expected
show_completed_models(completed_models)

#Preventing a Function from Modifying a List
#say that you start with a list of unprinted designs and write a function to move them to a list of completed models, as in the previous example. You may decide that even though you’ve printed all the designs, you want to keep the original list of unprinted designs for your records. But because you moved all the design names out of unprinted_designs, the
#......list is now empty, and the empty list is the only version you have; the original is gone. In this case, you can address this issue by passing the function a copy of the list, not the original. Any changes the function makes to the list will affect only the copy, leaving the original list intact.
#You can send a copy of a list to a function like this:
#...function_name(list_name[:])..... The slice notation [:] makes a copy of the list to send to the function.
#if we didn't want to empty the list of unprinted designs in printing_models.py we could call print_models() like this
print_models(unprinted_designs[:], completed_models)#NOTE: that this technique is done mainly when calling functions

#Passing an Arbitary Number of  Arguments
#Sometimes you won't know ahead of time how may arguments a function needs to accept.. Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.
#For example, consider a function that build a pizza. It needs to accept a number of toppings, but you can't know ahead of time how many toppings a person will want. The function in the following example has one parameter, *toppings, but this parameter collects as many arguments as the calling line provides:
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
make_pizza('Pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#The asterisk in the parameter name *toppings tells Python to make a empty tuple called toppings and pack whaetever value it recieves into this tuple. The print() call in the function body produces ouputs just to illustrate that now our function can handle a function with, one, three or so values.
#NOTE:Note that Python packs the arguments into a tuple, even if the function receives only one value:

#In our next example, we can replace the print() call with a loop that runs through the list of toppings and describes the pizza being ordered:
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#NOTE: This syntax works no matter how many arguments the function recieves.

#Trying with lists
def make_pizza(*toppings):
    """Trying to work with List in Arbitrary Arguments."""
    for topping in toppings:
        for name in topping:
            print(f"\n{name.title()}")
names = ['brian', 'loise', 'john']
cars = ['audi', 'rav4', 'harrier']
make_pizza(names)
make_pizza(names, cars)

#Mixing Positional and Arbitrary Arguments:
#If you want a function to accept several different kinds of aguments, the parameter that accepts an arbitary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remainig arguments in the final parameter>
#For example, if the function needs to take in a size for the pizza, that parameter must come before the parameter *toppings:
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#In the function definition, Python assigns the first value it receives to the parameter size. All other values that come after are stored in the tuple toppings. The funxtion calls include an argument for the size first, followed by as many toppings as needed.
#NOTE: You will often see the generic parameter name *args, which collects arbitrary positional arguments like this.


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
##NOTE:NOTE.NOTE:You will refer to pizza.py and making_pizza.py
#This first approach to importing, in which you simply write import followed by the name of the module, makes every function from the module available in your program. if you use this kind of import statement to import an entire module named module_name.py, each function in the module is available through the following syntax:
#........module_name.function_name()

#Importing Specific Functions
#You can also import a specific function from a module. Here's the general syntax for this approach:
#....from module_name import function_name
#You can import as many functions as you want from a module be separating each function's name with a comma:
#......from module_name import function_0, function_1, function_2
#Refer to making_pizza.py to see an illustration of how this would work
#With this syntax, you don’t need to use the dot notation when you call a function. Because we’ve explicitly imported the function make_pizza() in the import statement, we can call it by name when we use the function.

#Using as to Give a Function an Alias(Page 190 or 152)
#If the name of the function you are importing might conflict with an existing name in your program or if the function name is long, you can use a short, unique alias---an alternate name similar to a nickname when you import te function.
#.....Refer to making_pizza.py file...Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. The as Keyword renames a function using the alias you provide:
#The general syntax for providing an alias is:
#.....from module_name import function_name as fn

#Using as to Give a Module an Alias
#You can also provide an alias for a module name. Giving a module a short alias, like p for pizza, allows you to call the module's functions more quickly.
#Calling p.make_pizza() is more concise than calling pizza.make_pizza():
#Check example in making_pizza.py
#The module pizza is given the alias p in the import statement, but all of the module’s functions retain their original names. Calling the functions by writing p.make_pizza() is not only more concise than writing pizza.make_pizza(), but also redirects your attention from the module name and allows you to focus on the descriptive names of its functions. These function names,
#which clearly tell you what each function does, are more important to the readability of your code than using the full module name.
#The general syntax for this approach is:
#.....import module_name as mn

#Importing All Functions in a Module
#You can tell Python to import every function in a module by using the asterisk (*) operator:
#check on making_pizza.py
#NOTE:The asterisk in the import statement tells Python to copy every function from the module pizza into this program file. Because every function is imported, you can call each function by name without using the dot notation. However, it’s best not to use this approach when you’re working with larger modules that you didn’t write: if the module has a function name that matches an existing name in your project, you can get some unexpected results. Python may see several functions or variables with the
#..same name, and instead of importing all the functions separately, it will overwrite the functions. The best approach is to import the function or functions you want, or import the entire module and use the dot notation. This leads to clear code that’s easy to read and understand
#The general syntax for this approach is:
#........ from module_name import *

#Styling Functions
#You need to keep a few details in mind when you’re styling functions. Functions should have descriptive names, and these names should use lowercase letters and underscores. Descriptive names help you and others understand what your code is trying to do. Module names should use these conventions as well.
#Every function should have a comment that explains concisely what the function does. This comment should appear immediately after the function definition and use the docstring format. In a well-documented function, other programmers can use the function by reading only the description in the docstring. They should be able to trust that the code works as described, and as long as they know the name of the function,
#.....the arguments it needs, and the kind of value it returns, they should be able to use it in their programs.
#NOTE: If you speify a default value for a parameter, no space should be used on either side of the equal sign:
def function_name(parameter_0, parameter_1='default value'):
    print(f"{parameter_0}, {parameter_1}")
#The same convention should be used for keyword arguments in function calls:
function_name(value_0='', parameter_1='value')
#NOTE:If a set of parameters causes a function’s definition to be longer than 79 characters, press enter after the opening parenthesis on the definition line. On the next line, press tab twice to separate the list of arguments from the body of the function, which will only be indented one level.
#Most editors automatically line up any additional lines of parameters to match the indentation you have established on the first line:
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5
):
    """Function Body"""
    print('hello')
#If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins. All import statements should be written at the beginning of a file. The only exception is if you use comments at the beginning of your file to describe the overall program.


