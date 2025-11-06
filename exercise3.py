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