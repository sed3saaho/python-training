#(Page 128)
#Python's Dictionaries, will allow you to connect pieces of related information. You will learn how to access the information once it's in a dictionary and how to modify that information.
#because dictionaries can store an almost limitless amount of information:
#You will learn how to loop through the data in a dictionary. Additionally, you will learn to nest dictionaries inside lists, lists inside dictionaries, and even dictionaries inside other dictionaries.
#Understanding Dcitionaries allows you to model a variety of real world objects more accurately.You will be able to create a dictionary representing a person and the store as much information as you want about that person.
#you can store their name ,age , location, profession, and any other apesct of a person you can describe.
#You will be able to store any two kinds of information that can be matched up, such as a list of words and their meanings, a list of people's names and their favorite numbers

#Simple Dictionary:
#Consider a game featuring aliens that can have different colors and point values. This simple dictionary stores information about a oarticular alien:
alien_1 = {'color': 'green', 'points': 5}
print(alien_1['color'])
print(alien_1['points'])

person_1 = {'name':'Sedly Okolla', 'age':'26', 'nickname':'Saaho', 'wife':'Loise Okolla'}
print(person_1['name'])
print(person_1['age'])
print(person_1['nickname'])
print(person_1['wife'])
#Working with Dictionaries
#A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.
#A key's value can be a number, a string, a list, or even another dictionary. In fact you can use any object that you can create in python as a value in a dictionary.
#In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces, as shown in the earlier examples:
alien_1 = {'color':'green', 'points': 5}
#The keys in the above illustrations are "color" and "points" and there values are "green" and 5 respectively.
#NOTE: The collection of items in a dictionary are separated by a comma
#A key-value is a set of values associated with each other. When you provide a key, Python returns the value associated with that key
#Every key is connected to it's value by a colon, and individual key-value pairs are separated by commas. You can store as many key-value pairs as you want in a dictionary.
#Accessing Values in a Dictionary
#To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets as shown below
print(alien_1['color'])#This will return a value associated with that key which is "green"
#NOTE: you can have an unlimited number of key-value pairs in a dictionary.
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#Adding New Key-Value Pairs
#Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.
#To add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets along with the new value.
#In the example below we will add the x and the y coordinates of the position of the alien
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#To add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets along with the new value.
person_2 = {'name': 'Loise Mwende Okolla', 'age': '20'}
print(person_2)
person_2['Husband'] = 'Sedly Keith Okolla'
person_2['Hobby'] = 'Skating'
print(person_2)

#Starting with an Empty Dictionary
person_2 = {}
person_2['Name'] = 'Loise Mwende Okolla'
person_2['Age'] = 20
person_2['Hobby'] = 'Skating'
person_2['Husband'] = 'Sedly Keith Okolla'
print(person_2)

#Modifying Values in a Dictionary
#To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.
#Example: Consider a Value that changes from green to yellow as a game progresses
alien_o = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien color is now {alien_0['color']}.")

alien_0 = {'points': 5}
print(f"Your points are {alien_0['points']}.")
alien_0['points'] = 8
print(f"Your new Points are {alien_0['points']}")
#In our next example we want to track the position of an alien that can move at different speeds. We will store a value representing the alien's current speed
#and then use it to determine how far to the right the alien should move:
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original Position: {alien_0['x_position']}")
#Move the alien to the right
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien.
    x_increment = 3
#The new Position is the old postion plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#Removing Key-Value Pairs
#When you no longer need a piece of information that's stored in a dictionary, you can use the del statement to completely remove a key-value pair.
#All del needs is the name of the dictionary and the key you want to remove.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

#A Dictionary of Similar Objects
#The previous example involved storing different kinds of information about one object, an alien in a game for example. You can also use a dictionary to store one kind of information
#about many objects. For example, say you want to poll a number of people and ask them what their favorite programming language is. A dictionary is useful for storing the results of a simple poll like this:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
#When you know you will need more than one line to define a dictionary, press ENTER after the opening brace.
#Once you've finished defining the dictionary, add a closing brace on a new line after the last key-value pair and indent it one level so it aligns with keys in the dictionary
#It's good practise to include a comma after the last key-value pair as well, so you are ready to add a new key-value pair on the next line.
#To use this dictionary, given the name of a person who took the poll, you can easily look up their favorite language:
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite langauage is {language}.")

#Using get() to Access Values
#Using keys in square brackets to retrieve the value you're intersted in from a dictionary might cause one potential problem: if the key you ask for doesn't exist, you will get an error.
#You can use the get() method to set a default value that will be returned if the requested key doesn't exist
#The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn't exist:
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
#if the key 'points' exists in the dictionary, you will get the corresponding value. If it doesn't, you get the default value.
#if you leave out the second argument in the call to get() and the key doesn't exist, Python will return the value None.
dinner = {'starter': 'watermellon', 'drink': 'juice' , 'main_meal': 'ugali and kuku', 'desert': 'Cakes'}
order = dinner.get('starter', "Sorry but we dont have any starters at the moment")
print(order)

#Looping through an Dcitionary
#Dictionaries can be used to store information in a variety of ways; therefore, several different ways exist to loop through them.
#You can loop through all of a dictionary's key-value pairs, through it's keys, or through it's values.
user_1 = {
    'username': 'efermi',
    'first_name': 'enfrico',
    'last_name': 'fermi',
}
for key, value in user_1.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
#As shown above, to write a for loop for a dictionary, you create names for the two variables that will hold the key and the value in each key-value pair.
#You can choose any names you want for these two variables. for example above we could still replace it with the code below and it would still work fine
for k, v in user_1.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")
#The second half of the for statement includes the name of the dictionary followed by the method items(), which returns a list of key-value pairs.
#The "\n" in the first print call ensures that a blank line is inserted before each key-value pair in the output:
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_language.item():
    print(f"The favorite language of {name.title()} is {language.title()} ")
#This type of looping would work just as well if our dictionary stored the results from polling a thousand or even a million people.

#Looping through all the keys in a Dictionary
#The keys() method is useful when you don't need to work with all of the values in a dictionary. Let's loop through the favorite_language dictionary and print the names of everyone who took the poll:
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil' : 'python',
}
for name in favorite_language.keys():#Tells python to pull all the keys from the dictionary favorite_language and assigns them one at a time to the variable 'name'. The output shows the names of everyone who took the poll:
    print(name.title())
#Looping through the keys is actually the default behavior when looping through a dictionary, so the code below would have exactly the same output if you wrote....
for name in favorite_language:#You can use the keys() method explicitly if it makes your code easier to read, or you can omit if you wish.
    print(name.title)
#You can access the value associated with any key you care about inside the loop by using the current key , like in our case the current key is 'name'. Let's print a message to a couple of friends about the languages they chose.
#we'll loop through the names in the dictionary as we did previously, but when the name matches one of our friends, we will display a message about their favorite language:
favorite_language = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']#We make a list of friends that we want to print a message to.
for name in favorite_language.keys():#Inside the loop, we print each person's name.
    print(name.title())

    if name in friends:#We check whether the name we are working with is in the list 'friends'
        langauge = favorite_language[name].title()#if it is , we determine the person's favorite language using the name of the dictionary and the current value of name as the key
        print(f"\t{name.title()}, i see you love {language}!")#We then print a special greeting, including a reference to their language of choice. Everyone's name is printed, but our friends receive a special message:
#You can also use the keys() method to find out if a particular person was  polled. This time, let's find out if Erin took the poll:
favorite_language = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
} 
if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!")


#Exercise:
frienzies = {
    'stacy_B' : 'gordons',
    'stammily': 'general meakins',
    'marcel' : 'county brandy',
    'elina': 'captain morgan',
    'misky': 'gilbeys',
}
walevi = [ 'stammily', 'stacy_B']
criminal = (list(frienzies.keys())[-1],)
print(f"Criminal hapa naye si wote tunajua ni {criminal[0].title()} ")
for name in frienzies.keys():
    print(name)
    if name in walevi:
        print(f"Kama ni {name.title()} nayo tunaelewa cause wanachezea ligi ya akina {criminal[0].title()}, {frienzies[name].title()}!! Brooo!! ")
    if name not in walevi:
        print(f"{name.title()}, nayo tunasemanga ni wale wa kanisa , {frienzies[name].title()} si mbaya sanaa")
    if name in criminal:
        print(f"Eiiiiiiih!!! {name.title()}!!! , Criminal mwenyewe, ameamua kuendea {frienzies[name].title()} leo")
#The keys() method isn't just for looping: it actually returns a list of all the keys,

