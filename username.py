first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
user_age = input("Please enter your age: ")
user_age = int(user_age)

if user_age >= 13 :
	user_name = input("Please enter your username: ")
	print(f"Hello, {first_name.title()} {last_name.title()}. Are you sure that you want {user_name} as your username?")

	answer = input("Type yes to agree: ")

	if answer == 'yes': 
		print(f"Perfect, your username is {user_name}.")
	else:
		user_name = input("Please enter the correct username: ")
	print(f"Hello, {first_name.title()} {last_name.title()}. This is your new username: {user_name}")
else:
	years_left = 13 - user_age
	print(f"\nI'm sorry, you'll be able to access this in {years_left} years") 
