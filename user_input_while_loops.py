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
#NOTE: VEach time you use the input() function, you should include a clear, easy-to-follow prompt that tells the user exactly what kind of information you are looking for. Any statement that tells the user what to enter should work. For example:
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
#You can use a while loop to count up through a series of numbers. For example, the following while loop counts from 1 to 5:
current_number = 1# We start by counting from 1 by assigning current_number the value 1.
while current_number <= 5:#The while loop is then set to keep running as long as the value of current number is less than or equal to 5
    #The code inside the loop prints the value of current_number and then adds 1 to that value with current number += 1(The += operator is shorthand for current number = current_number + 1. )
    print(current_number)
    current_number += 1
#Python repeats the loop as long as the condition current_number <= 5 is true. Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2. Because 2 is less than 5, Python prints 2 and adds 1 again, making the current number 3, and so on. Once the value of current_number is greater than 5, the loop stops running and the program ends:
#A good example of how a while loop works..... a game needs a while loop to keep running as long as you want to keep playing, and so it can stop running as soon as you ask it to quit. Programs wouldn't be fun to use if they stopped running before we told them to or kept running even when we wanted to quit, so while loops are quite useful.

#Letting the User choose when to Quit.
#We can make the parrot program run as long as the user wants by putting most of the program inside a while loop. We'll define a quit value and then keep the program running as long as the user has not entered the quit value:
prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
#Explanation of the code above:
#we start by defing a prompt that tells the user their two options: entering a message or entering the 'quit' value. Then we set up a variable message that keeps track of whatever value the user enters. We define message as an empty string,"", so Python has something to check the first time it reaches the while line.
#.....The first time the program runs and Python reaches the while statement, it needs to compare the value of message to 'quit', but no user input has been entered yet. If Python has nothing to compare, it won't be able to continue running the program. To solve this problem, we make sure to give message an initial value. Although it's just an empty string, it will make sense to Python and allow it to perform the comparison that makes the while loop work.
#The while loop runs as long as the value of message is not 'quit'.
#The first time through the loop, message is just an empty string, so Python enters the loop. At message = input(prompt), Python displays the prompt and waits for the user to enter their input. Whatever they enter is assigned to message and printed; then Python reevaluates the condition in the while statement. As long as the user has not entered 'quit', the prompt is displayed again and Python waits for more input.
#When the user finally enters 'quit', Python stops executing the while loop and the program ends:

#Using a Flag.(page 158)
#In our previous examples, we had the program perform certain tasks while a given condition was true. But what about more complicated programs in which many different  events could cause the program to stop running?
#For example in a game, several different events can end the game. When the player runs out of ships, their time runs out out, or the cities they were supposed to protect are all destroyed, the game should end. it needs to end if any of these events happen.
#If many possible events might might occur to stop the program, trying to test all these conditions in one while statement becomes complicated and difficult.

#For a program that should run as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag,acts as a signal to the program....We can write our programs so they run while the flag is set to True and stop running when any several events set the value of the flag to False. As a result our overall while statement needs to check only one condition:
#......whether or not the flag is currently True. Then, all our other tests(to see if an event has occured that should set the flag to False) can be neatly organized in the rest of the program.
#
#Lets add a flag to our parrot.py from the previous section. This flag which we'll call active(though you can call it anything), will monitor whether or not the program should continue running:
prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
#We set the variable active to True, so the program starts in an active state. Doing so makes the while statement simpler because no comparison is made in the while statement itself; the logic is taken care of in other parts of the program
#As long as the active variable remains True, the loop will continue running
#in The if statement inside the while loop, we check the value of the message once the user enters their input, if the user enters 'quit' we set active to False, and the while loop stops. If the user enters anything other than 'quit' we print their input as a message. This program is similar to our previous one where we placed the conditional test derectly in the while statement. But now that we have a flag to indicate whether the overall program is in an active state.....
#.....it would be easy to add more tests(such as elif statements) for events that should cause active to become False.
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

#Using break to Exit a Loop
#To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.
#The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren't so the program only executes code that you want it to, when you want it to
#In our next example we are going to use break to end our while loop as soon as the use enters the 'quit' value
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit', 'escape', or 'exit' when you are finihed.) "
while True:# A loop that starts with with while True will run forever unless it reaches a break statement,
    city = input(prompt)
    #The loop in this program continues asking the user to enter the names of the  cities they have been until they enter 'quit'.... when they enter 'quit' 'exit' the break statement runs, causing Python to exit the loop:
    if city == 'quit':
        break
    elif city == 'exit':
        break
    elif city == 'escape':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
    
#Using continue in a Loop
#Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the begining of the loop based on the results of a conditional test.
#In our next example we are going to design a program that counts from 1 to 10 but prints only the odd numbers in that range.

#First we set the current_number to 0. Because it's less than 10,Python enters the while loop. Once inside the loop, we increment the count by 1 , so current number is 1. The if statement then checks the modulo of current_number and 2. If the modulo is 0 (which means current number is divisble by 2 )
#the continue statement tells Python to ignore the rest of the loop and return to the begining..If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number:
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#Avoiding infinite  Loops
#NOTE: Every while loop needs a way to stop running so it won't continue to run forever. For example, the counting loop below should count from 1 to 5:
x = 1
while x < 5:
    print(x)
    x += 1
#But id you accidentally omit the line x += 1 (as shown next), the loop will run forever:
#This loop runs forever!
x = 1
while x < 5:
    print(x)
#Now the value of x will start from 1 but never change. As a result, the conditional test x <= 5 will always evaluate to True and the while loop will run forever, printing a series of 1s,
#If your program gets stuck in an infinite loop, press CTRL-C or just close the terminal window displaying your program's output.



#Using a while loop with Lists and Dictionaries
#A for loop is effective  for looping through a list , but you should not modify a list inside a for loop because Python will have trouble keeping track of the items in the list. To modify a list as you work through it, use a while loop. Using the while loops with lists and dictionaries allows you to collect , store and organize lots of input to examine and report on later.

#Moving Items from One List to Another
#We are going to use a while loop to move newly registered users from the list of unverified users to a separate list of verified users after they have been verified
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#Page 163
while unconfirmed_users:#The while loop runs as long as the list of unconfirmed_users is not empty.
    current_user = unconfirmed_users.pop()#Within this loop the pop() function removes unverified users one at a time from the end of unconfirmed_users and assigns them to the  variable current_user
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

#Removing All instances specific values from a list
#In our previous programs we used remove() to remove a specific values from a list. but this only works well when the  value we want to remove appears only once in a list. But if you want to remove all instances of a value from a list, eg you have a list of pets and the value cat is repeated severally in the list , you can runn a while loop to remove all the instances of cat from the list until no value of cat exists in the list.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#Filling the dictionary with User Input
#You can prompt for as much input as you need in each pass through a while loop. Let’s make a polling program in which each pass through the loop prompts for the participant’s name and response. We’ll store the data we gather in a dictionary, because we want to connect each response with a particular user:

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
        polling_active = False#If they enter yes, the program enters the while loop again. If they enter no, the polling_active flag is set to False, the while loop stops running, and the final code block  displays the results of the poll.
#Polling is complete show results
print("\n------ Poll Results -------")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")