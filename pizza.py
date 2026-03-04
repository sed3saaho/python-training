#Refer to functions.py under the section of Sorting Your Functions in Modules
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
#We then Go ahead to make a separate file called making_pizza.py in the same directory as this file(pizza.py. This new file that we are creating imports the mosule we just created and then makes two calls to make_pizza())