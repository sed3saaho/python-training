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

