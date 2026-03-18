def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

class Dog:
    """A simple attemot to model a Dog"""
    def __init__(self, name, age):
        """Initalize name and age attributes"""
        self.dog_name = name
        self.dog_age = age
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.dog_name} is now sitting")
    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.dog_name} is rolling over")
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.dog_name}.")
print(f"My dog is {my_dog.dog_age} years old")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.dog_name}.")
print(f"You dog is {your_dog.dog_age} years old.")
your_dog.sit()
your_dog.roll_over()