#Refering to pizza.py from functions.py
import pizza
pizza.make_pizza(16, 'pepperoni')#This code produces the same output as the original program or code in functions.py that didn't import a module:
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions from it into this program.
#  You don't actually see the code being copied between files because Python copies the code behind the secens just before the program runs. All you need to know is that any function defined in pizza.py will now be available in making_pizza.py
#To call a function from an imported module, enter the name of the module you imported ,(pizza), followed by the name of the function,(make_pizza()), separated by a dot.

#Importing Specific functions
#More illustrations are in functions.py file
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#With this syntax, you don't need to use the dot notation when you call a function.Because we have explicity imported the function make_pizza() in the import statement, we can call it by name when we use the function.

#Using as to Give a Function an Alias
#More illustrations are in functions.py file
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
#Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. The as keyword renames a function using the alias you provide:
#The import statement shown here renames the function make_pizza() to mp() in this program. Any time we want to call make_pizza() we can simply write mp() instead, and Python will run the code in make_pizza() while avoiding any confusion with another make_pizza() function you might have written in this program file.
#The general syntax for providing an alias is:
#.....from module_name import function_name as fn

#Using as To Give a Module an Alias
#More illustrations are in functions.py file
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#The module pizza is given the alias p in the import statement, but all of the module’s functions retain their original names. Calling the functions by writing p.make_pizza() is not only more concise than writing pizza.make_pizza(), but also redirects your attention from the module name and allows you to focus on the descriptive names of its functions. These function names, which clearly tell you what each function does, are more important to the
#....readability of your code than using the full module name.
#The general syntax for this approach is:
#......import module_name as mn

#Importing All Functions in a Module
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#NOTE:The asterisk in the import statement tells Python to copy every function from the module pizza into this program file. Because every function is imported, you can call each function by name without using the dot notation. However, it’s best not to use this approach when you’re working with larger modules that you didn’t write: if the module has a function name that matches an existing name in your project, you can get some unexpected results. Python may see several functions or variables with the
#..same name, and instead of importing all the functions separately, it will overwrite the functions. The best approach is to import the function or functions you want, or import the entire module and use the dot notation. This leads to clear code that’s easy to read and understand
#The general syntax for this approach is:
#........ from module_name import *