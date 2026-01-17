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