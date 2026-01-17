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