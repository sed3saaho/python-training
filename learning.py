#title()method
name = "ada lovelace"
print(name.title())
#upper()method
name = "ada lovelace"
print(name.upper())
#lower()method
name = "ada lovelace"
print(name.lower())
#this will display 
#Ada Lovelace
#ADA LOVELACE
#ada lovelace
first_name = "Sedly"
second_name = "Keith"
#the f is is placed before the opening bracket
#Adding Whitespace to Strings with Tabs(\t) or Newlines(\t)
full_name = f"\n\t{first_name} \n\t{second_name}"
print(full_name.title())
#Stripping WhiteSpace
#to ensure that no white spaces exists on the right ,use(rstrip())
favorite_language = "python "
favorite_language.rstrip()
print(favorite_language)
#the one above removes the whitespace temporarily, 
#To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name i.e
favorite_dog = "Ruma "
favorite_dog = favorite_dog.rstrip()
print(favorite_dog)
#You can also strip whitespaces from the left side of a string using the (lstrip()) method, or from both sides using (strip())
# Syntax errors with strings on page 62
name = "erick omondi"
name = name.title()
greeting = f"Hello {name} How are you this fine morning"
print(greeting)

name = "erick omondi"
name = name.upper()
greeting = f"Hello {name} How are you this fine morning"
print(greeting)
#Numbers
#python uses two multiplication symbols to represent exponents
exponents = 3 ** 2 #equals 9
#Python supports the order of operations too, so you can use multiple operations in one expression.
#you can also use parantheses to modify the order of operations so Python can evaluate your expression in the order you specify example:
#2 +3*4 #will equal 14
# (2 + 3) * 4 equals 20
#When you divide two numbers, even if they are integers that result in a whole number , you will always get a float 4/2 = 2.0
#if you mix an integer and a float in any other operation, you will get a float as well: 1 + 2.0 = 3.0
#python defaults to a float in any operaton that uses a float, even if the output is a whole number

#Underscore in nummers
#when you are writing long numbers, you can group digits using underscores to make large numbers more readable:
universe_age = 14_000_000_000
#when you print a number that was defined using underscore,Python prints only the digits
print(universe_age)
#Multiple Assignment
#you can assign values to more than one variable using just a single line.
x,y,z = 1,2,3
#Constants
#When you want to treat a variable as a constant in your code, make the name of the variable all capital letters.
MAX_CONNECTIONS = 5000
#THE ZEN OF PYTHON( import this)

#LISTS
#lists are used to store a collection of items in a particular order.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#to access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets
#example when we want to access the first element in the list 
print(bicycles[0])
#you can also use the string methods on any elemnt in the list i.e
print(bicycles(0).title())
#index position starts from 0 and not 1
#python has a special syntax for accessing the last element in a list. By asking for the item at index -1,Python always returns the last item in the list:
print(bicycles[-1])
#this convention extends to other negative index values as well. The index-2 returns the second item from the end of the list, the index-3 returns the third item from the end, and so forth.
#using individual values from a list (page 73)
#you can use individual values in from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
#Changing,Adding, and Removing Elements in a list
#Most lists created are dynamic , meaning you can add and remove elements from it as your program runs its course
#the syntax for modyfying an element in the list is similar to the syntax for accessing an element in a list
#To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want the item to have
motorcycles = ['honda', 'yamaha', 'Suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#Adding elements to a list
#1.Appending Elemnts to the end of the list: the simplest way to add an element to a list is to append the item to the list.when you append an item to a list the new item is added to the end of the list
motorcycles.append('ducati')
print(motorcycles)
#The append() method makes it easy to build lists dynamically.For example, you can start with an empty list and then add items to the list using a series of append() calls.
#Example
vehicles = []
vehicles.append('Rav4')
vehicles.append('Range Rover')
vehicles.append('Mercedes Benz')
vehicles.append('Nissan')
vehicles.append('Lamboggini')
vehicles = vehicles.upper()
#Inserting Elements to a list
#You can add a new elemet at any position in your list by using the insert() method. You do this by specifying the index of the new element and the value of the new item
#In the example below The insert operation shifts every other value in the list one position to the right since it opens a postion at 0 and stores the value ducati.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
#Removing elements from a List
#You can remove an item according to its position in the list or according to it's value.
#Removing an item using thhe del statemnet
#if you know the postion of the item you want to remove from a list, you can use the del statement.
#you can remove any item from any position in a list using the del statement if you know it's index
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
#Removing an item using the pop() Method
#The pop method removes the last item in a list, but it lets you work with that item after removing it(page 77)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#We pop a value from the list and store that value in the variable popped_motorcycles
popped_motorcycles = motorcycles.pop()
print(motorcycles)
#we print the popped value to prove that we still have access to it after it has been removed from the list
print(popped_motorcycles)
#Popping items from any position in a List
#You can use pop to remove an item from any position in a list by including the index of the item you want to remove in parentheses.
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
#when you want to delete an item from a list and not use that item in  any way, use the del statement; if you want to use an item as you remove it. use the pop() method.

#Removing an item by value
#when you dont know the posistion of the value you want to remove from a list, and you only know the value of the item , you can use the remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
#You can also use the remove() method to work with a value that's being removed from a list. Let's remove the value 'ducati' and print a reason for removing it from the list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
#The remove method deletes only the first occurence of the value you specify.if there is a possibilty the value appears more than once in  the list, you will need to use a loop to make sure all occurences of the value are removed 

#ORGANIZING A LIST
#Sorting a List Permanently with the sort() Method
#The sort method changes the order of the list permanently.like in the example below the cars are sorted in an alphabeticall order and we can never revert to the original order
cars = ['bmw','audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#you can also sort the list in reverse alphabetical order by passing the argument reverse=True to the sort() method
cars = ['bmw','audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#sorting the list Temporarily with the sorted() Function
#The sorted function lets you display your list in a particular order but doesn't affect the actual order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again")
print(cars)
#The sorted() function can also accept a reverse=True argument if you want to display a list in reverse alphabetical order
#Printing a list in Reverse Order 
#To reverse the original order of a list, you can use the reverse() method///
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#Finding the length of a list
#You can quickly find the length of a list by using the len() function.
#it can be helpful in situations where you want to know the amount of data you are dealing with...like for example if you want to know the number of registered users on a website
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

#Looping through an entire list
#looping allows you to take the same action, or set of actions, with every item in a list.
#When you want to do the same action with every item in a list, you can use the Python's for loop
magicians = ['alice', 'david', 'carolina']
#we use the for loop to tell Python to pull a name from the list magicians, and associate it with the variable magician.
for magician in magicians:
#At this line we tell python to print the name that's just assigned to the variable magician
    print(magician)
#python then repeats lines 187 and 189 once for each name in the list:

workers = ['Fred', 'Violet', 'Henry', 'Sedly', 'Helenn', 'Elina', 'Lydia']
for name in workers:
    print(f"{name} is a worker in LAK LIQUOR")
#The concept of looping is important because it's one of the most common ways a computer automates repetitive tasks.
#Also keep in mind when writing your own for loops that you can choose any name you want for the temporary variable  that will be associated with each vaue in the list
#for cat in cats
#for dog in dogs
#for item in list_of_items:
#Using singular and plural names can help you identify whether a section of code is working with a single element from the lsit or the entire list.
#You can also write as many lines of code as you like in the for loop.Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list. Therefore, you can do as much work as you like with each value in the list.
#in practise you will often find it useful to do a number of different operations with each item in a list when you use a for loop.

#DOING SOMETHING AFTER A LOOP
#Usually you will want to summarize a block of output or move on to other work that your progran must accomplish after the loop is complete.
#Any lines of code after the loop that are not indented are executed only once without repetition.
#In Python, indentation is required to define which code belongs inside a block like:
#a function
#a loop
#a conditional (if, else)
#a class
#What makes a line indented in Python?
#indentation = Space or Tab at the begining of a line
#An identation line starts further to the right than the previous line.This tells Python that the line is inside a block of code_like a loop,function, or condition.
#Lets look at this:
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
#This shows that the two lines are indented since each begins with 4 spaces(or sometimes a tab) meaning they are indented under the for loop.
#Let's write a thank you message to the group of magicians as a whole,
#To display this group message after all the individual messages have been printed, we place the thank you message after the for loop without indentation:
#i.e:
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
#Making numerical lists
#Using the range() function
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
#The range() function is often used to create a list of numbers to loop through, or slice a list or a string
for value in range(1, 5):
    print(value)
#Although the code above looks like it should print the numbers from 1 to 5, it doesn't print the number 5 because range() doesn't include the last number in the sequence.This is another result of the off-by-one behaviour you'll see often in programming languages.(page 95)
#To include the last number in the sequence, you can add 1 to the second argument of the range() function:
for value in range(1, 6):
    print(value)
#To make a list of the first 10 numbers, you can call range() with no second argument:
for value in range(1, 11):
    print(value)
#To make a list of the first 10 numbers, you can call range() with no second argument:
numbers = list(range(1, 11))
#You can also pass range() only one argument, and it will start the sequence of numbers at 0.For example range(6) would return the numbers from 0 through to 5
for value in range(6):
    print(value)
#if you want to make a list of numbers, you can convert the result of range() directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.
numbers = list(range(1, 6))
print(numbers)
NUMBERS = list(range(1, 2))
print(NUMBERS)
#We can also use the range() function to tell Python to skip numbers in a given range.if you pass a third argument to range(). Python uses that value as a step size when generating numbers
#For example, here is how to list the even numbers between 1  and 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)
#in this example the range() function starts with the value 2 and then adds 2 to that value . it adds 2 repeatedly until it reaches or passes the end value, 11.
#you can create almost any set of numbers you want using the range() function.
#Lets make a list of the first 10 square numbers that is from 1 to 10
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
#Similar approach
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#SIMPLE STATISTICS WITH A LIST OF NUMBERS
#Some Python functions are useful when working with lists of numbers. For example you can easily find the minimum, maximum, and sum of a list of numbers:
digits = list(range(10))
print(digits)
minimum = min(digits)
maximum = max(digits)
summation = sum(digits)
print(minimum)
print(maximum)
print(summation)

#LIST COMPREHESSIONS( PAGE 97 )
#A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
#The following example builds the same list of square numbers you saw earlier but uses list comprehension:
squares = [value**2 for value in range(1, 11)]
print(squares)
#To use this syntax , begin with a descriptive name for the list, such as squares. Next, open a set of square brackets and define the expression for the values you want to store in the new list. in this example the expression is value**2 which raises the value to the second power.
#Then write a for loop to generate the numbers you want to feed into the expression, and close the square brackets
#The for loop in this example feeds the values 1 through 10 into the expression value**2.
#Notice that no colon is used at the end of the for statement

#WORKING WITH PART OF A LIST
#Slicing a List
#To make a slice, you specify the first and the last elements you want to work with.
#To output the first three elements in a list, you would request indices 0 htrough 3, which would return elements 0,1 and 2.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#If you want the second, third and fourth items in  a list, you would start the slice at index 1 and end at index four
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
#if you omit the first index in a slice, Python automatically starts your slice at the begining of the list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
#if you omit the second index in  a slice , python automatically begins from the first specified index to the end of the list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
#Recall that a negative index returns an element a certain distance from the end of a list
#for example if we want to output the last three players on the roster , we can use the slice player[-3:]
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
#if you include a third value in the brackets indicating a slice. this tells python how many items to skip between items in the specified range.
#list[start:stop:step]
# List of players
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Original list of players:")
print(players)

# Example 1: Take every 2nd player from the whole list
print("\nEvery 2nd player (players[::2]):")
print(players[::2])  # ['charles', 'michael', 'eli']

# Example 2: From index 1 to 4, skip every 2nd
print("\nPlayers from index 1 to 4, skipping one in between (players[1:5:2]):")
print(players[1:5:2])  # ['martina', 'florence']

# Example 3: Reverse the list
print("\nReversed list (players[::-1]):")
print(players[::-1])  # ['eli', 'florence', 'michael', 'martina', 'charles']

# Example 4: Get every 2nd name starting from index 1
print("\nEvery 2nd player starting from index 1 (players[1::2]):")
print(players[1::2])  # ['martina', 'florence']


#LOOPING THROUGH A SLICE
#You can use a slice in a for loop if you want to loop through a subset of the elements in a list.
players = ['charles', 'martina', 'michael', 'florence','eli']
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())
#Instead of looping through the entire list of the players python loops through only the first three names and prints their names

#COPYING A LIST
#Often you will want to start with an existing list and make an entirely new list based on the first one.
#To copy a list you can make a slice that includes the entire original list by omitting the first index and the second index( [:] ). This tells python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list
#For example, imagine we have a list of our favorite foods and want to make a separate list of foods that a friend likes. This friend likes everything in our list so far, so we can create their list by copying ours:
my_foods = ["pizza", "falafel", "carrot cake"]
friends_food = my_foods[:]
print("My favourite foods are:")
print(my_foods)
#Proving that we have two separate lists... by adding a new food to each list and showing that each list keeps track of the appropriate person's favorite foods:
my_foods.append('cannoli')
friends_food.append('ice_cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friends_food)

#TUPLES
#Python refers to values that cannot change as immutable and an immutable list is called a tuple
#A tupe looks exactly like a list except you use parenthesis instead of square brackets.once you define a tuple you can access individual elements by using each item's index, just as you would for a list
#For example, if we have a rectangle that should always be a certain size, we can ensure that it's size doesn't change by putting the dimensions into a tuple:
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#Tuples are technically defined by the presence of a comma; the parenthesis make them look neater and more readable. if you want to define a tuple with one element , you need to include a trailing comma:
my_t = (3,)#Tuple
#Looping through all value in a Tuple
for dimension in dimensions:
    print(dimension)
#Writing over a Tuple
#Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple.
#So if we wanted to change our dimensions, we could redine the entire tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModidfied dimensions:")
for dimension in dimensions:
    print(dimension)#Python doesn't raise any errors this time because reasigning a variable is valid:
#when compared with lists, tuples are simple data structures that are used when you want to store a set of values that should not be changed throughout the life of a program.


#STYLING YOUR CODE(PAGE 106)
#Appendix B shows you how to configure your text editor so it always inserts four spaces each time you press the tab key and shows a vertical guideline to help you follow the 79-character limit.

#if STATEMENTS
#programming oftenly involves examining a set of conditions and deciding which action to take based on those conditions.
#Python's if statements allows you to examine the current state of a progran and respond appropriately to that state.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#The loop in this example first checks if the current value of car is 'bmw'. If it is, the value is printed in uppercase. if the value of the car is anything other than 'bmw', it is printed in title case
#Testing for equality is case sensitive in Python. For example two value with different capitalization are not considerede equal:
#If case matters, this behavior is advantageous. But if case doesn't matter and instead you just want to test the value of the a variable , you can convert the variable's value to lowercase before doing the comparison:
car = 'Audi'
car.lower() == 'audi'
#Checking for inequality
requested_topping = ['mushrooms', 'banana', 'anchoives']
for topping in requested_topping:
   if topping != 'anchoives':
       #To insert a variable's value into a string, use f strings
       print(f"{topping}\tHold the anchoives")
   else:
       print(f"{topping}\tWhat the helly")

#Conditional Statements with numbers
numbers = list(range(0,11,2))
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
ages = list(range(1,23))
for age in ages:
    if age >= 18:
        print(f"Since you are {age} years old you are older enough to use our site.....WELCOME!!")
    else:
        print(f"Sorry, until you are old enough you are not permitted to use our sight. you are just {age} yaers old")
#Each mathematical comparison can be used as part of an if statement, which can help you detect the exact conditions of interest.:( = , < , > , =< , >= , % 2 == 0) and many other more
#Checking Multiple Conditions
#For example sometimes you might need two conditions to be True to take an action. Other times you might be satisfied with just one condition being True. The keywords AND and OR can help you in these situations.
#Using and to Check Multiple Conditions
#To check whether two conditions are bothy True simultaneously, use the keyword " and " to combine the two conditional tests; if each test passes, the overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.
#Example, checking if two people are both over 21
person_1 = 18
person_2 = 22
if person_1 >= 21 and person_2 >= 21:
    print("They are both over 21")
else:
    print("Some of the above conditions have not been met")

person_3 = 23
person_4 = 24
if person_3 >= 21 and person_4 >= 21:
    print("They are both over 21")
else:
    print("Some of the above conditions have not been met")
#Using " or " to check multiple conditions
#The keyword " or " allows you to check for multiple conditions as well, but it passes when either or both of the individual tests pass. An " or " expression fails only when both individual tests fail
#This time we will look id at least one person is 21
person_1 = 19
person_2 = 20
if person_1 >= 21 or person_2 >= 21:
    print("At least one of them is 21")
else:
    print("None of them is over 21")

person_3 = 23
person_4 = 17
if person_3 >= 21 or person_4 >= 21:
    print("At least one of them is 21")
else:
    print("None of them is over 21")

#Checking whether a value is in a List( page 114)
#To find whether a particular value is already in a list, use the keyword " in "
#We will make a list of toppings a customer has requested for a pizza and then check whether certain toppings are in the list.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("CORRECT")
else:
    print("NULL")
#This technique is powerfull  because you can create a list of essential values and then easily check whether the value you are testing matches one of the values in the lsit

#Checking Whether a Value is Not in a List
#You can use the keyword " not  in " in this situation
#For example consider a list of users who are banned from commenting in a forrum, you can check whether a user has been banned before allowing that person to submit a comment:
banned_users = ['andrew', 'carolina', 'david']
user = ['juliet', 'jane', 'andrwe', 'david']
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"{user.title()} sorry but you are banned from posting a comment")
#The if-else structure works well in situations in which you want Python to always execute one of two possible actions.

#The if-elif-else Chain
#Often you will need to test more than two possible situations, and to evaluate these you can use Python's if-elif-else syntax. Python executes only one block in an if-elif-else chain. it runs each conditional test in order until one passes. when atest passes, the code following that test is executed and python skips the rest of the tests.
#For example consider an amusement park that charges different rates for different age groups.
# Admission for anyone under age 4 is free.
#Admission for anyone between the ages of 4 and 18 is $25.
#Admission for anyone age 18 or older is $40.
# we want to use the if statement to determine a person's admission rate
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
#Different approach
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
#Using Multiple elif Blocks.
#You can use as many elif blocks in your code as you like.
age = 65
if age < 4:
    price = 0
elif age < 8:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}")

#Omitting the else Block

