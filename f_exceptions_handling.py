#Exceptions(page 232/ 194)

#Python uses special objects called exceptions to manage errors that arise during a program's execution.
#Whenever an error occurs that makes Python unsure what to do next, it creates an exception object.
# If you write code that handles the exceptions, the program will continue running. If you don't handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.
#Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised.
#When you use try-except blocks, your programs will continue running even if things start to go wrong. Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you write

#Handling the ZeroDivisionError Exception
#Let’s look at a simple error that causes Python to raise an exception. You probably know that it’s impossible to divide a number by zero, but let’s ask Python to do it anyway:
print(5/0) # of course Python can't do this , so  we get a traceback: when we run it
#The error reported  in the traceback, ZeroDivisionError, is an exception object. Python creates this kind of object in response to a situation where it can’t do what we ask it to. When this happens, Python stops the program and tells us the kind of exception that was raised. We can use this
#...information to modify our program. We’ll tell Python what to do when this kind of exception occurs; that way, if it happens again, we’re prepared.

#Using try_except Blocks
#When you  think an error may occur, you can write a try_except block to handle the exception that might be raised. You tell Python to try running some code, and you tell it what to do if the code reults in a particular kind of exception.
#Below is what a try_except block for handling the ZeroDivisionError exception looks like:
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
#We put print(5/0), the line that caused the error, inside a try block. If the code in a try block works, Python skips over the except block. If the code in the try block causes an error, Python looks for an except block whose
#......NOTE: error matches the one that was raised and runs the code in that block.
#In this example, the code in the try block produces a ZeroDivisionError, so Python looks for an except block telling it how to respond. Python then runs the code in that block, and the user sees a friendly error message instead of a traceback:
#If more code followed the try-except block, the program would continue running because we told Python how to handle the error. 

#Let’s look at an example where catching an error can allow a program to continue running.

#Using Exceptions to Prevent Crashes
#Handling errors correctly is especially important when the program has more work to do after the error occurs. This happens often in programs that prompt users for input. If the program responds to invalid input appropriately, it can prompt for more valid input instead of crashing
#Example: Let's create a simple calculator that does only division:
print("Give me two numbers, and i will divide them. ")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
#This program avove does nothing to handle errors, so asking it to divide by zero causes it to crash:
#The else Block.....Page(234 or 196)
#We can make this program more error resistant by wrapping the line that might produce errors in a try-except block. The error occurs on the line that performs the division, so that’s where we’ll put the try-except block.
#This following example also includes an else block. Any code that depends on the try block executing successfully goes in the else block:
print("Give me two numbers, and i will divide them. ")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:#We ask Python to try complete the division operation in a try block, which includes only the code that might cause an error
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:#The except block tells Python how to respond when a ZeroDivisionError arises. If the try block doesn’t succeed because of a division by zero error, we print a friendly message telling the user how to avoid this kind of error
        print("You can't divide by 0!")
    else:#Any code that depends on the try block succeeding is added to the else block. In this case if the division operation is successful, we use the else block to print the result.
        print(answer)
#This program is now more resistant to errors. If the user tries to divide by zero, they get a friendly error message instead of a traceback, and the program continues running. The user can keep trying to enter numbers until they decide to quit. The program continues to run, and the user never sees a traceback:

#NOTE: NOTE: More Explanations
#The try-except-else block works like this: Python attempts to run the code in the try block. The only code that should go in a try block is code that might cause an exception to be raised. Sometimes you’ll have additional code that should run only if the try block was successful; this code goes in the else block. The except block tells Python what to do in case a
#....certain exception arises when it tries to run the code in the try block. By anticipating likely sources of errors, you can write robust programs that continue to run even when they encounter invalid data and missing resources. Your code will be resistant to innocent user mistakes and malicious attacks.



#Handling the FileNotFoundError Exception
#One common issue when working with files is handling missing files. The file you’re looking for might be in a different location, the filename may be misspelled, or the file may not exist at all. You can handle all of these
#...situations in a straightforward way with a try-except block.
#Let’s try to read a file that doesn’t exist. The following program tries to read in the contents of Alice in Wonderland, but I haven’t saved the file alice.txt in the same directory as alice.py:
filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    contents = f.read()
#There are two changes here. One is the use of the variable f to reprsent the file object, which is a common convention. The second is the use of the encoding argument. This argument is needed when your system's default encoding doesn't match the encoding of the file that's being read.
#In the above example Python can't read from  a missing file, so it raises an exception when you run it.The last line of the traceback reports a FileNotFoundError: this is the exception Python creates when it can’t find the file it’s trying to open. 
#In this example, the open() function produces the error, so to handle it, the try block will begin with the line that contains open():
filename = 'alice.txt'
try:
    with open(filename, 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
#In the example above, the code in the try block produces a FileNotFoundError, so Python looks for an except block that matches that error. Python then runs the code in that block, and the result is a friendly error message instead of a traceback:....Sorry, the file alice.txt does not exist.



#Analyzing Text
#You can analyze text files containing entire books. Many classic works of literature are available as simple text files because they are in the public domain. The texts used in this section come from Project Gutenberg (http://gutenberg.org/). Project Gutenberg maintains a collection of literary works that are
#...available in the public domain, and it’s a great resource if you’re interested in working with literary texts in your programming projects
#working with literary texts in your programming projects.
#Let’s pull in the text of Alice in Wonderland and try to count the number of words in the text. We’ll use the string method split(), which can build a list of words from a string. 
#The split() method separates a string into parts wherever it finds aspace and stores all the parts of the string in a list. The result is a list of words from the string, although some punctuation may also appear with some of the words. 
#To count the number of words in Alice in Wonderland, we’ll use split() on the entire text. Then we’ll count the items in the list to get a rough idea of the number of words in the text:
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist. ")
else:
    #Count the approximate number of words in the file.
    words = contents.split()#We take the string contents, which now contains the entire text of Alice in Wonderland as one long string, and use the split() method to produce a list of all the words in the book.
    num_words = len(words)#we use len() on the list to examine it's length, which will give us a good approximation of the number of words in the original string.
    print(f"The file {filename} has about {num_words} words. ")#This code is placed in the else block because it will work only if the code in the try block was executed successfully. The output tells us how many words are  in alice.txt......The file alice.txt has about 29465 words.
#Explanation
#If we moved the alice.txt to the correct directory, the try block will work .



#Working with Multiple Files
#Let’s add more books to analyze. But before we do, let’s move the bulk of this program to a function called count_words(). By doing so, it will be easier to run the analysis for multiple books:
def count_words(filename):
    """Count the approximate number of words in  a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filename = 'alice.txt'
count_words(filename)
#we can proceed write a simple loop to count the words in any text we want to analyze. We do this by storing the names of the files we want to analyze in a list, and then we call count_words() for each file in the list. We’ll try toncount the words for Alice in Wonderland, Siddhartha, Moby Dick, and Little
#...Women, which are all available in the public domain. I’ve intentionally left siddhartha.txt out of the directory containing word_count.py, so we can see how well our program handles a missing file:
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
#NOTE: The missing siddhartha.txt file has no effect on the rest of the program’s execution:
#Using the try-except block in this example provides two significant advantages. We prevent our users from seeing a traceback, and we let the program continue analyzing the texts it’s able to find. If we don’t catch the FileNotFoundError that siddhartha.txt raised, the user would see a full
#...traceback, and the program would stop running after trying to analyze Siddhartha. It would never analyze Moby Dick or Little Women.


#Failing Silently
#In the previous example, we informed our users that one of the files was unavailable. But you don’t need to report every exception you catch. Sometimes you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened. To make a program fail silently, you
#....write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a pass statement that tells it to do nothing in a block:
def count_words(filename):
    """Count the approximate number of words in  a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
       pass #here is the pass statement
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
 count_words(filename)
 #Now when a FileNotFoundError is raised, the code in the except block runs, but nothing happens. No traceback is produced, and there’s no output in response to the error that was raised. Users see the word counts for each file that exists, but they don’t see any indication
...#that a file wasn’t found
#NOTE; NOTE: The pass statement also acts as a placeholder. It’s a reminder that you’re choosing to do nothing at a specific point in your program’s execution and that you might want to do something there later. For example, in this program we might decide to write any missing filenames to a file called
#...missing_files.txt. Our users wouldn’t see this file, but we’d be able to read the file and deal with any missing texts.


#Deciding which Errors to Report
#How do you know when to report an error to your users and when to fail silently? If users know which texts are supposed to be analyzed, they might appreciate a message informing them why some texts were not analyzed. If users expect to see some results but don’t know which books are supposed
#...to be analyzed, they might not need to know that some texts were unavailable. Giving users information they aren’t looking for can decrease the usability of your program. Python’s error-handling structures give you finegrained control over how much to share with users when things go wrong; it’s up to you to decide how much information to share.

#Well-written, properly tested code is not very prone to internal errors, such as syntax or logical errors. But every time your program depends on something external, such as user input, the existence of a file, or the availability of a network connection, there is a possibility of an exception being raised. A little experience will help you know where to include exception
#...handling blocks in your program and how much to report to users about errors that arise.