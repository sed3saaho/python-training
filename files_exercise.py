#Exrecise 1
filename = 'piexercise.txt'
with open(filename, 'w') as file_object:
    name = input("What's Your name? ")
    file_object.write(f"{name}\n")

#Exercise 2

filename = 'piexercise.txt'
with open(filename, 'a') as file_object:
    active = True
    while active:
        name = input("Please type in your name or 'quit' to Quit: ")
        if name != 'quit':
            print(f"Hello {name}. Hope you are doing Well")
            file_object.write(f"{name} will be paying as a visit\n")
        else:
            active = False

#Exrecise 3
filename = 'piexercise.txt'
with open(filename, 'a') as file_object:
    active = True
    while active:
        name = input("Please Provide your name, or type 'quit' to Quit: ")
        if name == 'quit':
            active = False
        else:
            poll = input(f"{name.title()} Please tell us why you like programming or type 'quit' to Quit: ")
            if poll != 'quit':
                print(f"Thank you so much {name.title()} for your response have a nice time")
                file_object.write(f" The reason why {name.title()} likes programming is {poll}")
            else:
                active = False
            

#EXCEPTION
#Exercise 1
print("Give me two numbers and then i will add them for you")
first_number = input("Enter the 1st number: ")
second_number = input("Enter the 2nd Number: ")

try:
    total = int(first_number) + int(second_number)
    print(f"The Sum of {first_number} and {second_number} is: {total}")
except ValueError:
    if type(first_number) != int:
        print(f"{first_number} is not an integer")
    else:
        print(f"{second_number} is not an integer")

#Exercise 2
active = True
while active:
    print("\nGive me two numbers and then i will add them for you; type quit to Quit")
    
    first_number = input("\tEnter the 1st number: ")
    if first_number == 'quit':
        break
        
    second_number = input("\tEnter the Second number: ")
    if second_number == 'quit':
        break

    try:
        # Try to convert both. If either fails, it jumps to 'except'
        total = int(first_number) + int(second_number)
        print(f"\tThe sum of {first_number} and {second_number} is: {total}")
        
    except ValueError:
        # Check which one specifically is not a digit
        if not first_number.isdigit():
            print(f"\tSorry, '{first_number}' is not an integer.")
        else:
            print(f"\tSorry, '{second_number}' is not an integer.")
            

        




