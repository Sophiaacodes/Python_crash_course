'''here we have the pets all stored with their own definition, so that we can use the classes made with specific data'''
from dog import Pet, Dog #importing multiple categories

#defining my animals
my_parrot = Pet('alejandro', 105)
my_dog = Dog('John', 27)
your_dog = Dog('Bianca', 102)
#different characteristics
your_dog.describe_fur = 'black'
my_parrot.update_favorite_toy = 'mouse'


#general pet
print(f"I've got a {my_parrot.age} years old parrot called {my_parrot.name.title()}")
print(f"{my_parrot.name.title()} has a {my_parrot.update_favorite_toy} with which he plays")

#my dog
print(f"\nMy dog's name is {my_dog.name}")
print(f"My dog's is {my_dog.age} years old")
my_dog.update_favorite_toy()
my_dog.food.describe_food()
my_dog.describe_fur()
my_dog.sit()

#your dog
print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog's is {your_dog.age} years old")
print(f"your dog has {your_dog.describe_fur} fur")
your_dog.update_favorite_toy()
your_dog.sit()