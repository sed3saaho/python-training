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
print(greet_user._doc_)#accessing the docstring at runtime
help(greet_user)#using the help fuction to generate the documentation of a given function from the docstring


#Passing informtion to a Function
#We wiil modify our previous function so as to include the name of the user while greeting them
#For the function to greet the user by name, you enter username or name or name1........ in the parenthesis of the function's definition at def greet_user(). By adding username here you allow the function to accept any value of username you specify.
#.........The function will now expect you to provide a value for username eac time you call it. When you call greet_user(), you can pass it a name, such as 'jesse' inside the parantheses:
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