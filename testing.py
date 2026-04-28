#TESTING YOUR CODE(Page 247 OR  209)
#When you write a function or a class, you can also write tests for that code. Testing proves that your code works as it’s supposed to in response to all the input types it’s designed
#...to receive. When you write tests, you can be confident that your code will work correctly as more people begin to use your programs. You’ll also be able to test
#...new code as you add it to make sure your changes don’t break your program’s existing behavior. Every programmer makes mistakes, so every programmer must test their code often, catching problems before users encounter them.

#In this chapter you’ll learn to test your code using tools in Python’s unittest module. You’ll learn to build a test case and check that a set of inputs results in the output you want. You’ll see what a passing test looks like and what a failing test looks like, and you’ll learn how a failing test can
#......help you improve your code. You’ll learn to test functions and classes, and you’ll start to understand how many tests to write for a project.


#Testing a Function
#To learn about testing , we need code to test. Below is a simple function that takes in a first and last name, and returns a neatly formatted full name:
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
#The function get_formatted_name() combines the first and last name with a space in between to complete a full name, and then capitalizes and returns the full name.
#To check that get_formatted_name() works, let's make a program that uses this function. The program below let's users enter a first and last name, and see a neatly formatted full name:
print("Enter 'q' at any time to quit")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
formatted_name = get_formatted_name(first, last)
print(f"\tNeatly formatted name: {formatted_name}.")