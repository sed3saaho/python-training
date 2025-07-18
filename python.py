digits = list(range(10))
print(digits)
minimum = min(digits)
maximum = max(digits)
summation = sum(digits)
print(minimum)
print(maximum)
print(summation)
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
#List comprehension
cubes = list((value**3 for value in range(1, 11)))
print(cubes)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])