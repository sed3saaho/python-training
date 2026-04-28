#Reading an entire file
with open ('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
#Explanatons
#The first line of this program has a lot going on. Let's start by looking at the open() function. To do any work with a file, even just printing it's contents, you first need to open the file to access it.
#The open() function needs one argument: The name of the file you want to open. Python looks for this file in the directory where the program that's currently being executed is stored. In our example files_exceptions.py is currently running, so Python looks for pi_digits.txt in the directory where files_exeptions.p is stored.
#The open() function returns an object returns an object representing the file. Here, open('pi_digits.txt') returns an object representing pi_digits.txt . Python assigns this object to file_object, which we will work with later in the program.
#The keyword with closes the file once access to it is no longer needed.
#NOTE: Notice how we call open() in this program but not close(). You could open and close the file by calling open() and close(), but if a bug in your program prevents the close method from being executed, the file may never close. Improperly closed files can cause data to be lost or corrupted. And if you call close() too early in your program ,you will find yourself trying to work with a closed file (a file you can't access), which leads to more errors.
#It’s not always easy to know exactly when you should close a file, but with the structure shown here, Python will figure that out for you. All you have to do is open the file and work with it as desired, trusting that Python will close it automatically when the with block finishes execution
#Once we have a file object representing pi_digits.txt, we use the read() method in the second line of our program to read the entire contents of the file and store it as one long string in contents. When we print the value of contents, we get the entire text file back:


#FILE PATHS
#When you pass a simple filename like pi_digits.txt to the open() function, Python looks in the directory where the file that’s currently being executed (that is, your .py program file) is stored.
#Sometimes, depending on how you organize your work, the file you want to open won’t be in the same directory as your program file. For example, you might store your program files in a folder called python_work; inside python_work, you might have another folder called text_files to distinguish your program files from the text files they’re manipulating. Even though text_files is in python_work, just passing open() the name of a file in text_files won’t work, because Python will only look in python_work and stop there; it won’t go on and look in text_files. To get
#......Python to open files from a directory other than the one where your program file is stored, you need to provide a file path, which tells Python to look in a specific location on your system.
#Because text_files is inside python_work, you could use a relative file path to open a file from text_files. A relative file path tells Python to look for a given location relative to the directory where the currently running program file is stored. For example, you’d write:
#  with open('text_files/filename.txt') as file_object:
#This line tells Python to look for the desired .txt file in the folder text_files and assumes that text_files is located inside python_work (which it is). 
#You can also tell Python exactly where the file is on your computer regardless of where the program that’s being executed is stored. This is called an absolute file path. You use an absolute path if a relative path doesn’t work. For instance, if you’ve put text_files in some folder other than python_work—say, a folder called other_files—then just passing open() the
#...path 'text_files/filename.txt' won’t work because Python will only look for that location inside python_work. You’ll need to write out a full path to clarify where you want Python to look.
#Absolute paths are usually longer than relative paths, so it’s helpful to assign them to a variable and then pass that variable to open():
#   file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
#   with open(file_path) as file_object:
#Using absolute paths, you can read files from any location on your system. For now it’s easiest to store files in the same directory as your program files or in a folder such as text_files within the directory that stores your program files.



#Reading line by line
#When you’re reading a file, you’ll often want to examine each line of the file. You might be looking for certain information in the file, or you might want to modify the text in the file in some way. For example, you might want to read through a file of weather data and work with any line that includes the word
#....sunny in the description of that day’s weather. In a news report, you might ook for any line with the tag <headline> and rewrite that line with a specific kind of formatting.
#You can use a for loop on the file object to examine each line from a file one at a time:
filename = 'pi_digits.txt'

with open(filename) as file_object:#NOTE: Whene we call open , an object representing the file and it's contents is assigned to the variable file_object
    for line in file_object:# To examine the file's contents, we work through each line in the file by looping over the file object
        print(line)


#Making a List of lines from a file
#When you use with, the file object returned by open() is only available inside the with block that contains it. If you want to retain access to a file’s contents outside the with block, you can store the file’s lines in a list inside the block and then work with that list. You can process parts of the file immediately and postpone some processing for later in the program.
#The following example stores the lines of pi_digits.txt in a list inside the with block and then prints the lines outside the with block:
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()#readlines() method takes each line from the file and stores it in a list. The list is then assigned to the variable lines, which we can continue to work with after the with block ends.
for line in lines:# we use a sinple for loop to print each line from lines.
    print(line)


#Working with a File's Contents.
#After you’ve read a file into memory, you can do whatever you want with that data, so let’s briefly explore the digits of pi. First, we’ll attempt to build a single string containing all the digits in the file with no whitespace in it:
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()#We start by opening the file and storing each line of digits in a list

pi_string = ''  #we create a variable, pi_string, to hold the digits of pi.
for line in lines:#We then create a loop that adds each line of digits to pi_string and removes the newline character from each line 
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

#NOTE: When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the int() function or convert it to a float using the float() function.
#Examples:
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()


numbers = float(pi_string)
addition = 1 + numbers
print(addition)

#Example 2
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        # Convert the string to a float to do math
        number = float(line) 
        print(number * 2)
#NOTE: Pro-Tip: Cleaning the Data Text files often have invisible "newline" characters at the end of lines. Use .strip() to clean them before converting:



#Large Files: One Million Digit
#So far we’ve focused on analyzing a text file that contains only three lines, but the code in these examples would work just as well on much larger files. If we start with a text file that contains pi to 1,000,000 decimal places
#.....instead of just 30, we can create a single string containing all these digits. We don’t need to change our program at all except to pass it a different file. We’ll also print just the first 50 decimal places, so we don’t have to watch a million digits scroll by in the terminal:
file_name = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")
print(len(pi_string))
#Python has no inherent limit to how much data you can work with; you can work with as much data as your system’s memory can handle.


#Is  your birthday contained in Pi
#I’ve always been curious to know if my birthday appears anywhere in the digits of pi. Let’s use the program we just wrote to find out if someone’s birthday appears anywhere in the first million digits of pi. We can do this
#....by expressing each birthday as a string of digits and seeing if that string appears anywhere in pi_string:
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter Your birthday in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appear in the first million digits od pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")



#Writing to a File
#One of the simplest ways to save data is to write it to a file. When you write text to a file, the output will still be available after you close the terminal containing your program’s output. You can examine output after a program finishes running, and you can share the output files with others as well. You
#......can also write programs that read the text back into memory and work with it again later.

#Writing to an Empty File
#To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file.. To see how this works, let's write a simple messsage and store it in a file instead of printing it to the screen
filename = 'pi_write.txt'

with open(filename, 'w') as file_object:# We use the write() method on the file object to write a string to the file. This program has no terminal output, but if you open the file pi_write.txt, you will see one line .... i love programming
    file_object.write("I love programming")
#The call to open in the above example has two arguments. The 1st argument is still the name of the file we want to open. The 2nd argument 'w' tells Python that we want to open the file in write mode. You can open a file in read mode ('r'), write mode ('w'), append mode('a'), or a module that allows you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in read_mode by default.
#NOTE: The open() function automatically creates the file you are writing to if it doesn't already exist. However, be careful opening a file in write mode ('w') because if the file does exist, Python will erase the contents of the file before returning the file object.
#NOTE: The file created behaves like any other file on your computer. You can open it, write new text in it, copy from it, paste to it, and so forth.
#NOTE: Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.


# Writing Multiple Lines
#NOTE: The write() function doesn’t add any newlines to the text you write. So if you write more than one line without including newline characters, your file may not look the way you want it to:
filename = 'pi_programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
#Icluding newline characters in your calls to write() makes each string appear on it's own line, because if you were to omit them or not include them , then when you open the file you are writing to then you will see  the two lines squished together.....Eg,..I love programming.I love creating new games.
#You can also use spaces, tab characters, and blank lines to format your output, just as you’ve been doing with terminal-based output.

#Appending to a File:
#If you want to add content to a file instead of witing over existing content, you can open the file in append mode ('a'). When you open a file in append mode ('a'), Python doesn't erase the contents of the file before returning the file object.
#Any lines you write to the file will be added at the end of the file. NOTE: If the file doesn't exist yet, Python will create an empty file for you.
#Let’s modify our code by adding some new reasons we love programming to the existing file pi_programming.txt:
filename = 'pi_programming.txt'

with open(filename, 'a') as file_object:# We use the 'a' argument to open the file for appending rather than writing over the existing file.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser\n")
#We will end up with the original contents of the file, followed by the new content we just added.