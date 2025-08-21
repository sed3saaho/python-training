name = "erick omondi"
name = name.title()
greeting = f"Hello {name} How are you this fine morning"
print(greeting)

name = "erick omondi"
name = name.upper()
greeting = f"Hello {name} How are you this fine morning"
print(greeting)

authors_name = "Albert Einsten"
quote = '"A person who never made \n a mistake never tried anything new"'
expression = f"{authors_name} once said {quote}."
print(expression)

favorite_number = 5
message = f"my favorite number is {favorite_number}"
print(message)

#LISTS
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
print(bicycles[-1].title())
print(bicycles(1))

names = ['violet', 'fred', 'henry', 'sedly', 'lencer', 'hellen', 'elina']
owner = f"The owner and the CEO of LAK LIQUOR PARLOUR is {names[-3].title()}"
print(owner)
print(f"{names[0].title()} is a worker at LAK LIQUOR")
print(f"{names[1].title()} is a workerr at LAK LIQUOR")
print(f"{names[2].title()} is a worker at LAK LIQUOR")
print(f"{names[3].title()} is a worker at LAK LIQUOR")
print(f"{names[-2].title()} is a worker at LAK LIQUOR")
print(f"{names[-1].title()} is a worker at LAK LIQUOR")
#Changing the value of am element in the lis
motorcycles = ['honda', 'yamaha', 'Suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
#Appending an element to the list using the append('string') method
motorcycles.append('Boxer')
print(motorcycles)

vehicles = []
vehicles.append('Rav4')
vehicles.append('Range Rover')
vehicles.append('Mercedes Benz')
vehicles.append('Nissan')
vehicles.append('Lamboggini')
print(vehicles)
#Inserting elements into a list using the insert(index, 'string') method
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
#Removing an item from a list using the del statemnet
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
#Removing an item from the list usinng pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#We pop a value from the list and store that value in the variable popped_motorcycles
popped_motorcycles = motorcycles.pop()
print(motorcycles)
#we print the popped value to prove that we still have access to it after it has been removed from the list
print(popped_motorcycles)
#You can use pop to remove an item from any position in a list by including the index of the item you want to remove in parentheses.
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#Removing an item by value
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

guests = ['Muga', 'Rock', 'Bonnie', 'Symo', 'Brad']
#while calling a value in a list use square brackets[] and not brackets()
print(f"{guests[0]} i take this chance to welcome you to my dinner this evening")
print(f"{guests[1]} i take this chance to welcome you to my dinner this evening")
print(f"{guests[2]} i take this chance to welcome you to my dinner this evening")
print(f"{guests[3]} i take this chance to welcome you to my dinner this evening")
print(f"{guests[4]} i take this chance to welcome you to my dinner this evening")

not_coming = guests.pop(-1)
print(f"I take this chance to announce that {not_coming} wont be coming for the dinner")
guests.append('Barry')
print(guests)
print(f"{guests[0]} i take this chance to welcome you to my dinner this evening")
print(f"{guests[1]} i take this chance to welcome you to my dinner this evening")
print(f"{guests[2]} i take this chance to welcome you to my dinner this evening")
print(f"{guests[3]} i take this chance to welcome you to my dinner this evening")
print(f"{guests[4]} i take this chance to welcome you to my dinner this evening")

guests.insert(0,'Elina')
guests.insert(3, 'Lydia')
guests.append('Rolex')
print(guests)
print("I am sorry to you all for the inconvenience but due to unavoidable circumstances i here by announce to you that only a maximum of two will be allowed for dinner")
guest_1 = guests.pop(1)
guest_2 = guests.pop(-2)
guest_3 = guests.pop(-4)
guest_4 = guests.pop(2)
guest_5 = guests.pop(-3)
guest_6 = guests.pop(1)

print(guests)
del guests[0]
del guests[0]
print(guests)

#sorting list in alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#sorting the lsit in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
#Sorting a list temporarily using the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again")
print(cars)
#Printing the list in Reverse order using the reverse() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#Finding the length of a List using the len() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

#Looping through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can wait to see your next trick, {magician.title()}.\n")
#Concept of indentation
print(f"Thank you, everyone. That was a great magic show!")
    

workers = ['Fred', 'Violet', 'Henry', 'Sedly', 'Helenn', 'Elina', 'Lydia']
for name in workers:
    print(f"{name} is a worker in LAK LIQUOR")

#Using the range() function
for value in range(1,5):
    print(value)
for value in range(1, 6):
    print(value)
for value in range(1, 11):
    print(value)
for value in range(6):
    print(value)
#Making a list of numbers
numbers = list(range(1, 6))
print(numbers)

NUMBERS = list(range(1, 8))
print(NUMBERS)
#using range() to skip numbers in a given range
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

#Simple Statistics with a List of Numbers
digits = list(range(10))
print(digits)
minimum = min(digits)
maximum = max(digits)
summation = sum(digits)
print(minimum)
print(maximum)
print(summation)
#List Comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

numbers = list(range(1, 1_000_000))
maximum = max(numbers)
minimum = min(numbers)
total = sum(numbers)
print(maximum)
print(minimum)
print(total )

odd_numbers = list(range(1,20,2))
print(odd_numbers)

# Create a list of multiples of 3 from 3 to 30
multiples_of_three = list(range(3, 31, 3))

# Use a for loop to print each number
for number in multiples_of_three:
    print(number)
    # Create an empty list to store the cubes
cubes = []

# Use a for loop to generate cubes from 1 to 10
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# Print each cube
for cube in cubes:
    print(cube)

cubes = list((value**3 for value in range(1, 11)))
print(cubes)
#slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#COPYING A LIST
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
#Working with Tuples
available_foods = ("Pilau", "Matumbo", "Kuku", "Nyama Choma", "Eggs")
for food in available_foods:
    print(food)
available_foods = ("Rice", "Mtura", "Kuku", "Nyama Choma", "Eggs")
print('\nModified foods')
for food in available_foods:
    print(food)

#if STATEMENTS
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
requested_topping = ['mushrooms', 'banana', 'anchoives']
for topping in requested_topping:
   if topping != 'anchoives':
       print(f"{topping}\tHold the anchoives")
   else:
       print(f"{topping}\tWhat the helly")
#Conditional statements with numbers
numbers = list(range(0,11))
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

#Using the keyword " and " to check multiple conditions:
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

#Using the Keyword " or " to check multiple conditions:
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

#Checking whether a value is in a List using the keyword " in "
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("CORRECT")
else:
    print("NULL")

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







