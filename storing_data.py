#Many of your programs will ask users to input certain kinds of information. You might allow users to store preferences in a game or provide data for a visualization. Whatever the focus of your program is, you’ll store the information users provide in data structures such as lists and dictionaries. When
#....users close a program, you’ll almost always want to save the information they entered. A simple way to do this involves storing your data using the json module.
#The json module allows you to dump simple Python data structures into a file and load the data from that file the next time the program runs. You can also use json to share data between different Python programs. Even better,
#...the JSON data format is not specific to Python, so you can share data you store in the JSON format with people who work in many other programming languages. It’s a useful and portable format, and it’s easy to learn.

#The JSON (JavaScript Object Notation) format was originally developed for JavaScript. However, it has since become a common format used by many languages, including Python.

# """Using json.dump() and json.load()"""
#Let's write a short program that stores a set of numbers and another program that reads these numbers back into memory. The first program use json.dump() to store the set of numbers, and the second program will use json.load()
#The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data.
#Below is how you can use json.dump() to store a list of numbers:
import json

numbers = [2,3,5,7,11,13]
filename = 'numbers.json'#we choose a filename in which to store the list of numbers: NOTE: It's customary to use the file extension .json to indicate that the data in the file is stored in the JSON format.
with open(filename, 'w') as f:#Then we open the file in write mode to allow json to write the data to the file.
    json.dump(numbers, f)#here we use the json.dump() function to store the list numbers in the file number.json.
    #This program has no output, but if you opne the file numbers.json, you will find that our data is stored in a format that looks just like Python: [2, 3, 5, 7, 11, 13]

#Now we will write a program that uses json.load() to read the list back into memory:
import json

filename = 'numbers.json'#here we make sure to read from the exact file that we want
with open(filename) as f:#This time we open the file in read mode because Python only needs to read from the file.
    numbers = json.load(f)#Here we use the json.load() function to load the information stored in numbers.json, and we assign it to the variable numbers.

print(numbers)#Finally we print the recovered list of numbers 



#Saving and Reading User-Generated Data
#Saving data with json is useful when you’re working with user-generated data, because if you don’t store your user’s information somehow, you’ll lose it when the program stops running. Let’s look at an example where we prompt the user for their name the first time they run a program and then remember their name when they run the program again.
#Let’s start by storing the user’s name:
import json
username = input("What is your name? ")#We prompt for a username to store. Next we use json.dump(), passing it a username and a file object, to store the username in a file
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you comeback, {username}!")

#Now let’s write a new program that greets a user whose name has already been stored:
import json
filename = 'username.json'
with open(filename) as f:
    username = json.load(f)#we use json.load() to read the information stored in username.json and assign it to the variable username.
    print(f"Welcome back, {username}!")

#We need to combine these two programs into one file. When someone runs remember_me.py, we want to retrieve their username from memory if possible; therefore, we’ll start with a try block that attempts to recover the username. If the file username.json doesn’t exist, we’ll have the except block
#.....prompt for a username and store it in username.json for next time:
import json
"""Load the username if it has been stored previously
   Otherwise, Prompt for the username and store it"""

filename = 'username.json'
try:
#we try to open the file username.json. If this file exists, we read the username back into memory and print a message welcoming back the user in the else block. 
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
#If this is the first time the user runs the program, username.json won’t exist and a FileNotFoundError will occur. Python will move on to the except block where we prompt the user to enter their username . We then use json.dump() to store the username and print a greeting.
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
#Whichever block executes, the result is a username and an appropriate greeting. If this is the first time the program runs, this is the output:
    





#Refactoring
#Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. This process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend. 
#We can refactor remember_me.py by moving the bulk of its logic into one or more functions. The focus of remember_me.py is on greeting the user, so let’s move all of our existing code into a function called greet_user():
import json

def greet_user():
    """Greet user by name."""
    filename = 'username.json' 
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name?")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}")

greet_user()
#the function greet_user() is doing more than just greeting the user—it’s also retrieving a stored username if one exists and prompting for a new username if one doesn’t exist. Let’s refactor greet_user() so it’s not doing so many different tasks.
#.....We’ll start by moving the code for retrieving a stored username to a separate function:

import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username  = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
#The new function get_stored_username() retrieves a stored username and returns the username if it finds one. If the file username.json doesn’t exist, the function returns None v. This is good practice: a function should either return the value you’re expecting, or it should return None. This allows us to perform a simple test with the return value of the function.
#We should factor one more block of code out of greet_user(). If the username doesn't exist, we should move the code that prompts for a new username to a function dedicated to that purpose:
import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username  = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

#Each function above has a single, clear purpose. We call greet_user(), and that function prints an appropriate message: it either welcomes back an existing user or greets a new user. It does this by calling get_stored_username(), which is responsible only for retrieving a stored username if one exists. Finally, greet_user() calls get_new_username()
#....if necessary, which is responsible only for getting a new username and storing it. This compartmentalization of work is an essential part of writing clear code that will be easy to maintain and extend.



#Exercises:(page 246 OR 208)

#Exrecise 1

def getting_favorite_number():
    """Getting user favorite number"""
    favorite_number = int(input("What is your favorite number? "))
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)

def displaying_favorite_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        print("No favorite number stored yet. ")
    else:
        print(f"I know your favorite number! it's {favorite_number}")
        

#Exercise 2
import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username  = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
#The main part of the Question
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        verify =input(f"Is {username} your actual username? ")
        if verify == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()



