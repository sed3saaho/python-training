#User input and while loops
age = input("How old are you? ")
age_1 = int(age)
if age_1 >= 18:
    print("You are an adult")
else:
    print("Sorry you are still too Young")

height = input("How tall are you, in inches? ")
height_0 = int(height)
if height_0 >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you are a little taller.")

number = input("Enter a number, and i will tell you if it's even or odd: ")
number_0 = int(number)
if number_0 % 2 == 0:
    print(f"\nThe number {number_0} is even.")
else:
    print(f"The number {number_0} is odd")
    
#While loops:
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number = current_number + 1#This line applys the same anology as the one below
    current_number += 1#This is the shorthand of the one above
    
#Using Flags
prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "Enter 'quit', 'exit' or 'escape' to end the program: "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    elif message == 'exit':
        active = False
    elif message == 'escape':
        active = False
    else:
        print(message)

#Using break to Exit a loop
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit', 'escape', or 'exit' when you are finihed.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    elif city == 'exit':
        break
    elif city == 'escape':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


responses = {}
#Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
#Polling is complete show results
print("\n------ Poll Results -------")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")



#eXTENSIONS THAT I AINT SURE ABOUT
name = input("Tell me your name then i text you something: ")
name2 = name.title()
notorious = ['Bonnie','Brad','Pididy']
good_boys = ['Gift', 'Sedly', 'Symo']
if name2 in notorious:
    print(f"{name2} damn!! you are a bad boy")
elif name2 in good_boys:
    print(f"{name2} I can see you are a good boy")
else:
    print(f"{name2} you do not exist")
    

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


responses = {}
#Set a flag to indicate that polling is active.
polling_active = True

while polling_active:#As long as polling_active is true, Python will run the code in the while loop.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
#Polling is complete show results
print("\n------ Poll Results -------")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

    

    