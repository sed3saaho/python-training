#Dictionaries
alien_1 = {'color': 'green', 'points': 5}
print(alien_1['color'])
print(alien_1['points'])

person_1 = {'name':'Sedly Okolla', 'age':'26', 'nickname':'Saaho', 'wife':'Loise Okolla'}
print(person_1['name'])
print(person_1['age'])
print(person_1['nickname'])
print(person_1['wife'])

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

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

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite langauage is {language}.")

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
#Will print the value associated with the starter
dinner = {'starter': 'watermellon', 'drink': 'juice' , 'main_meal': 'ugali and kuku', 'desert': 'Cakes'}
order = dinner.get('starter', "Sorry but we dont have any starters at the moment")
print(order)
#Will print the default value since we dont have the key starter
dinner = { 'drink': 'juice' , 'main_meal': 'ugali and kuku', 'desert': 'Cakes'}
order = dinner.get('starter', "Sorry but we dont have any starters at the moment")
print(order)
#looping through a dictionary.
user_1 = {
    'username': 'efermi',
    'first_name': 'enfrico',
    'last_name': 'fermi',
}
#The items() method
for key, value in user_1.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_language.items():
    print(f"The favorite language of {name.title()} is {language.title()} ")
#The keys() method
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil' : 'python',
}
for name in favorite_language.keys():
    print(name.title())

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil' : 'python',
}
friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_language[name].title()
        print(f"/t{name.title()}, I see you love{language}")
    
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil' : 'python',
}
if 'erin' not in favorite_language.keys():
    print("Erin, please take our poll!")

frienzies = {
    'stacy_B' : 'gordons',
    'stammily': 'general meakins',
    'marcel' : 'county brandy',
    'elina': 'captain morgan',
    'misky': 'gilbeys',
}
walevi = [ 'stammily', 'stacy_B']
criminal = (list(frienzies.keys())[-1],)#Tuple
print(f"Criminal hapa naye si wote tunajua ni {criminal[0].title()} ")
for name in frienzies.keys():
    print(name)
    if name in walevi:
        print(f"Kama ni {name.title()} nayo tunaelewa cause wanachezea ligi ya akina {criminal[0].title()}, {frienzies[name].title()}!! Brooo!! ")
    if name not in walevi:
        print(f"{name.title()}, nayo tunasemanga ni wale wa kanisa , {frienzies[name].title()} si mbaya sanaa")
    if name in criminal:
        print(f"Eiiiiiiih!!! {name.title()}!!! , Criminal mwenyewe, ameamua kuendea {frienzies[name].title()} leo")

#Sorting the keys in a dictionary using the sorted function
favorite_langauge = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_language.keys ()):
    print(f"{name.title()}, thank you for taking the poll.")
#Looping through All the Values in a Dictionary
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())
#Using a set in the following example below:
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'violet': 'ruby',
    }
print("The following languages have bee mentioned, we are using a set in this example:")
for language in set(favorite_language.values()):
    print(language.title())
#Defining a Set:
languages = {'python', 'ruby', 'c', 'python', 'ruby', 'javascript'}
print(languages)
#Using list comprehension in the example below:
languages = {'python', 'ruby', 'c', 'python', 'ruby', 'javascript'}
titled_languages = [lang.title() for lang in languages]
print(sorted(titled_languages))

#Exercises:
rivers = {
    'yala': 'kenya',
    'nile': 'egypt',
    'amazon': 'brazil',
    'niger': 'nigeria',
    'orange': 'south africa',
    }
for river in rivers.keys():
    print(f"The River {river} runs trough {rivers[river]}")
#Similar approach
rivers = {
    'yala': 'kenya',
    'nile': 'egypt',
    'amazon': 'brazil',
    'niger': 'nigeria',
    'orange': 'south africa',
    }
for river, country in rivers.items():
    print(f"The River {river} runs through {country}")

rivers = {
    'yala': 'kenya',
    'nile': 'egypt',
    'amazon': 'brazil',
    'niger': 'nigeria',
    'orange': 'south africa',
    }
for river in rivers.keys():
    print(river.title())

rivers = {
    'yala': 'kenya',
    'nile': 'egypt',
    'amazon': 'brazil',
    'niger': 'nigeria',
    'orange': 'south africa',
    }
for river in rivers.keys():
    print(rivers[river].title())
#Exercise 3(page  143)
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'violet': 'ruby',
    }
poll_takers = ['fred', 'elina', 'jen', 'sarah', 'edward', 'phil', 'violet', 'bazenga']
for name in poll_takers:
    if name in favorite_language.keys():
        print(f"Thank you {name.title()}, for your response")
    if name not in favorite_language.keys():
        print(f"Hello {name.title()}, am here to remind you that earlier on you were invited to take a poll on the language you love")
#Nesting Dictionaries
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
#Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
#Nesting lists inside a Dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print(f"/n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
#Different and more accurate approach:
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'Fred': ['javascript'],
    }
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favvorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite langauge is :")
        for language in languages:
            print(f"\t{language.title()}")
#Nesting a Dictionarie in a dictionary 
users = {
    'aeinstein': {
        'firstname': 'albert',
        'lastname': 'einstein',
        'location': 'princeton',
    },
    'murcie': {
        'firstname': 'marie',
        'lastname': 'curie',
        'location': 'paris',
    },
    'violet': {
        'firstname': 'adhiambo',
        'lastname': 'akeyo',
        'location': 'bondo',
    },
}
for username, user_info in users.items():
    print(f"\n Username: {username}")
    full_name = f"{user_info['firstname']} {user_info['lastname']}"
    location = user_info['location']

    print(f"\t Full name: {full_name.title()}")
    print(f"\t Location: {location.title()}")

#Exercise 1 page(150)
person_1 = {
    'name': 'sedly keith',
    'age': 26,
    'nickname': 'saaho',
    'hobby': 'bodybuilding',
}
person_2 = {
    'name': 'loise mwende',
    'age': 23,
    'nickname': 'miss saaho',
    'hobby': 'roll ball',
}
person_3 = {
    'name': 'elina yvett',
    'age': 23,
    'nickname': 'dongonyado',
    'hobby': 'watching',
}
people = [person_1, person_2, person_3]
for person in people:
    name = person['name']
    age = person['age']
    nickname = person['nickname']
    hobby = person['hobby']
    print(f"\n{name.title()}'s details are:")
    print(f"\tAge: {age}")
    print(f"\tNickname: {nickname.title()}")
    print(f"\tHobby: {hobby.title()}")
#Exercise 2
pet_1 = {
    'owner name': 'sedly keith',
    'pet name': 'ruma',
    'animal kind': 'dog',
    'pet age': '5 years',
}
pet_2 = {
    'owner name': 'loise mwende',
    'pet name': 'cutie',
    'animal kind': 'cat',
    'pet age': '2 years',
}
pet_3 = {
    'owner name': 'elina yvett',
    'pet name': 'greace',
    'animal kind': 'chiwawa',
    'pet age': '3 years',
}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    pet_name = pet['pet name']
    pet_owner = pet['owner name']
    animal_kind = pet['animal kind']
    pet_age = pet['pet age']
    print(f"\nThe following are the details of {pet_name.title()}")
    print(f"\t The Owner of the pet is {pet_owner.title()} ")
    print(f"\tThe kind of animal {pet_name.title()} is, is a {animal_kind.title()}")
    print(f"\tAnd the age of {pet_name.title()} is {pet_age} old")
#Exercise 3
favorite_places = {
    'fred': ['nairobi', 'homabay', 'siaya', 'kericho', 'naivasha'],
    'violet': ['gwasi', 'bondo', 'suna'],
    'lydia': ['kisumu', 'akala', 'ugunja', 'nakuru']
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
#Exercise 4
favorite_numbers= {
    'fred': [2,4,6,8,10],
    'violet': [1,3,5,7,9],
    'lydia': [12,14,16,18,20],
    'elina': [21,33,25,47,59],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: {numbers}")

#Exercise 5
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13_960_000,
        'language': 'japanese',
        'famouse landmark': 'tokyo tower',
        'currency': 'Japanese Yen (JPY)',
        'fact': 'Tokyo is the most populous metropolitan area in the world, with over 37 million people living in its greater region.',
    },
    'paris': {
        'country': 'france',
        'population': 2_160_000,
        'language': 'french',
        'famouse landmark': 'eiffel tower',
        'currency': 'Euro(EUR)',
        'fact': 'The Eiffel Tower was originally meant to be a temporary structure for the 1889 Worlds Fair — it was almost torn down afterward!',

    },
    'nairobi': {
        'country': 'kenya',
        'population': 4_400_000,
        'language': 'swahili and english',
        'famouse landmark': 'nairobi national park',
        'currency': 'Kenyan Shilling (KES)',
        'fact': 'The city s iconic Times Square was named after The New York Times newspaper in 1904.'

    },
}
for city, city_info in cities.items():
    print(f"\nBelow are the details of {city.upper()}, City")
    country = city_info['country']
    population = city_info['population']
    language = city_info['language']
    famouse_landmark = city_info['famouse landmark']
    currency = city_info['currency']
    fact = city_info['fact']
    print(f"\tIts a city in {country.title()}")
    print(f"\tThe population in this {city.title()} is roughly {population}")
    print(f"\tThe popular language in {city.title()} is {language.title()}")
    print(f"\tThe famouse landmark in {city.title()} is {famouse_landmark.title()}")
    print(f"\tThe currency used is {currency}")
    print(f"\tAnd a common fact about {city.title()} is: {fact}")



#Additional points to note while working with Dictionaries
#NOTE: Using the update() method to Add one or multiple key-value pairs; You can add pairs from another dictionary or from an iterable of key-value pairs.
person = {'name': 'Alice'}
print(person)
person.update({'age': 20, 'city': 'paris'})
print(person )

#NOTE: setdefault() ; Add a key only if it doesn't  exist
person = {'name': 'Alice'}
print(person)
person.setdefault('age', 20)
print(person)
person.setdefault('name', 'Bob')#Wont change existing value
print(person)

#NOTE: Dictionary unpacking(**) ; Creates a dictionary by merging dictionaries
dict1 = {'a':1 , 'b': 3}
print(dict1)
dict2 = {'ogago': 4 , 'nyonds': 43}
print(dict2)
new_dict = {**dict1, **dict2}
print(new_dict)

#Pop method ; Remove a key and return it's vale
person = {'name': 'Alice', 'age': 20, 'city': 'Paris'}
print(person)
age = person.pop('age')
print(age)
print(person)

 
#popitem() Remove and return the last inserted key-value pair; Removes the most recently added item
person = {'name': 'Alice', 'age': 20, 'city': 'Paris'}
print(person)
item = person.popitem()
print(item)
print(person)


#clear() Remove all items; Empties the dictionary completely.
person = {'name': 'Alice', 'age': 20, 'city': 'Paris'}
print(person)
person.clear()
print(person)

#Dictionary comprehension (create a new dictionary) Removes items by condition while creating a new dictionary.
#NOTE: This does not modify the original dictionary
person = {'name': 'Alice', 'age': 20, 'city': 'Paris'}
filtered_person = {k : v for k, v in person.items() if k != 'age'}
print(filtered_person)



#Additional practise:
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'speed': 'slow', 'points':5}
    aliens.append(new_alien)
print(len(aliens))
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    
print(aliens[:5])
for alien2 in aliens[:5]:
    if alien2['color'] == 'green':
        alien2['color'] = 'yellow'
        alien2['speed'] = 'medium'
        alien2['points'] = 10
    elif alien2['color'] == 'yellow':
        alien2['color'] = 'red'
        alien2['speed'] = 'fast'
        alien2['points'] = 15
for final_alien in aliens:
    print(final_alien)
    




