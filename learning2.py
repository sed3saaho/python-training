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