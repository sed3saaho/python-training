#The Python standard library is a set of modules included with every Python installation.
#Now that you have a basic understanding of how functions and classes work, you can start to use modules like these that other programmers have written.
#You can use any function or class in the standard library by including a simple import statement at the top of your file.

#Let's look at one module, random, which can be us=6ful in modeling many real-world situations.
#One interesting function from the random module is randint() This function takes two integer arguments and returns a randomly selected integer between(and including) those numbers. Below is how to generate a random number between 1 and 6:
from random import randint

print(randint(1,6))

 #Another useful function is choice(). This function takes in a list or tuple and returns a randomly chosen element.
 
from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

workers = ['fred', 'violet', 'elina', 'sharon', 'brenda']
print(choice(workers))

#NOTE: The random module should't be used when building security-related applications, but it's good enough for many fun and interesting projects.
