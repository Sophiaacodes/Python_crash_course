'''go to my_dog.py to see the results here there are just the classes 4 definition'''
#a function that's a part of a class is called a method
class Pet: #capitalization is used for classes
	'''simple attempt to model a dog'''

	def __init__(self, name, age): #the __init__() method is a method runned by py whenever we create a new instance based on that class
		'''initialize name and age attributes'''
		self.name = name #self paramether is required and gives the individual instance access to the attributes and methods in the class
		self.age = age

	def update_favorite_toy(self, toy):
		#set the toy to a given value
		self.favorite_toy = toy

class Food:
	'''attempt to model food for a dog'''

	def __init__(self, g_kibbles=75):
		'''initialize food attributes'''
		self.g_kibbles = g_kibbles

	def describe_food(self):
		'''print statement describing food'''
		print(f"This dog needs {self.g_kibbles}g of food")

class Dog(Pet): 
	'''simple attempt to model a dog'''

	def __init__(self, name, age): 
		'''initialize attributes from parent class'''
		super().__init__(name, age)
		self.color_fur = 'white'
		self.food = Food()

	def describe_fur(self):
		#printing a statement for fur color
		print(f"{self.name} has a {self.color_fur} fur")

	def sit(self):
		#simulation dog sitting in response to a command
		print(f"{self.name} is now sitting")

	def roll_over(self):
		#simulation dog rolling over in response to a command
		print(f"{self.name} is now rolling over")

	def update_favorite_toy(self):
		#overwriting the parent script
		print(f"There's no other toy for dogs than chewbecca")



