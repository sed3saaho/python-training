# When your program needs a name , you will be able to prompt the user for a name. When your program need a list of names, you will be able to prompt the user for a series of names. To do this you will use the input() function.
#You will also learn how to keep programs running as long as users want them to, so they can enter as much information as they need to; then, your program can work with that information. You will use Python's while loop to keep programs running as long as certain conditions remain true.
#With the ability to work with user input and the ability to control how long your programs run, you will be able to write fully interactive programs.

#How the input() Function works
#The input function pauses your program and waits for the user to enter some text. Once Python receives the user's input, it assigns that input to a variable to make it convenient for you to work with.
#For example, the following program asks the user to enter some text, then displays that message back to the user:
message = input("Tell me something, and i will repeat it back to you:")
print(message)
 #NOTE: The input() function  takes one argument: the 'prompt', or instructions, that we want to display to the user so they know what to do. In the above example when python runs the first line, the user sees the prompt 'Tell me something and i will repeat it back to you:'
 #.....the program waits while the user enters their response and continues after the user presses ENTER. The response is assigned to the variable message, then the print(message) displays the input back to the user:

#Writing Clear Prompts
#Each time you use the input() function, you should include a clear, easy-to-follow prompt that tells the user exactly what kind of information you are looking for. Any statement that tells the user what to enter should work. For example:
name = input("Please enter your name: ")#Add a space at the end of your prompts(after the colon) to separate the prompts from the user's response and to make it clear to your user where to enter their text
print(f"\nHello, {name.title()}")
#NOTE Sometimes you will want to write a prompt that is longer than one line. For example, you might want to tell the user why you are asking for certain input. You can assign your prompt to a variable and pass that variable to the input function. This allows you to build your prompt over several lines, then write a clean input() statement.
prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your first name?"
name = input(prompt)
print(f"\nHello, {name}")
#This example shows one way to build a multi-line string. The first line assigns the first part of the message to the variable prompt. In the second line the operator += takes the string that was assigned to prompt and adds the new string onto the end.
#The prompt now spans two line, again with space after the question mark for clarity:

#Using int() to Accept Numerical input
#When you use the input function, Python interprets everything the user enters as a string. Consider the following interpreter session, which asks for the user's age:
age = input("How old are you? ")
print(age)
#The user enters the number 21 for example, but when we ask Python for the value of age it returns '21', the string representation of the numerical value entered. We know python interpreted the input as a string because the number is now eclosed in quotes. 
#If all you want to do is print the input, this works well. But if you try to use the input as a number, you will get an error:
age = input("How old are you? ")
if age >= 18:#This is going to give you a TypeError because the age will be presented as a string instead of a number.
    print("You are an adult")
#When you try to use the input to do a numerical comparison python produces an error because it can't compare a string to an integer.
#We can resolve this issue by using the int() function, which tells Python to treat the input as a numerical value
#The int() function converts a string representation of a number to a numerical representation, as shown below:
age = input("How old are you? ")
age_1 = int(age)
if age_1 >= 18:
    print("You are an adult")
else:
    print("Sorry you are still too Young")
#In the example above, when we eneter 21 at the prompt, Python interprets the number as a string, but the value is then converted to a numerical representation by int()

height = input("How tall are you, in inches? ")
height_0 = int(height)
if height_0 >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you are a little taller.")
#The program can compare height to 48 because height_0 = int(height) converts the input value to a numerical representation before the comparison is made.
#NOTE When you use numerical input to do calculations andd comparisons,be sure to convert the input value to a numerical representation first.

#The Modulo Operator
#A useful tool for working with numerical information is the modulo operator (%) which divides one number by another number and returns the remainder:
#The modulo operator doesn't tell you how many times one number fits into another, it just tells you what the remainder is. When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0 in such kind of cases. You can use this fact to determine whether a number is even or odd.
number = input("Enter a number, and i will tell you if it's even or odd: ")
number_0 = int(number)
if number_0 % 2 == 0:
    print(f"\nThe number {number_0} is even.")
else:
    print(f"The number {number_0} is odd")


#Introducing while Loops
#The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while loop runs as long as , or while, a certain condition is true.
#The while Loop in Action:
#You can use a while loop to count up through a series of numbers. For exa