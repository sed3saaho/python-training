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
for name, language in favorite_language.item():
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
if 'erin' not in favorite_language.key():
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