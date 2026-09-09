def greet_user(username):
	'''display a simple greeting''' #comment called docstring
	print(f'Hello, {username.title()}')

greet_user('jess')

def greet_user(name, surname):
	print(f'Hello, {name.title()} {surname.title()}')

greet_user('jess', 'mariano')
greet_user(name = 'rory', surname = 'gilmore')
greet_user(surname='gilmore', name='loralai')

def greet_user(name, surname='gilmore'):
	print(f'Hello, {name.title()} {surname.title()}')

greet_user('emily')
greet_user(name='richard')
greet_user('luke', 'danes') #in case it changes you can just change the value

#RETURN VALUE
def get_formatted_name(name, surname):
	'''return full name formatted'''
	full_name = f"{name} {surname}"
	return full_name.title()

musician = get_formatted_name('patricia', 'laCosta')
print(f'Miss Patty full name is {musician}')

#optional middle name
def get_formatted_name(name, surname, middle=''):
	'''return full name formatted'''
	if middle:
		full_name = f"{name} {middle} {surname}"
	else:
		full_name = f"{name} {surname}"
	return full_name.title()

musician = get_formatted_name('patricia', 'laCosta')
print(f'Miss Patty full name is {musician}')

musician = get_formatted_name('patricia', 'laCosta', 'Miss Patty')
print(musician)

def build_person(name, surname, age=None):
	'''return a dictionary of information about a person'''
	person = {'first_name' : name, 'last_name' : surname}
	if age: #using a list allows u to get more informations and add them in the function also
		person['age'] = age
	return person

student = build_person('paris', 'geller', age=20)
print(student)

