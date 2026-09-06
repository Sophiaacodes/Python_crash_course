Agnes = {'age': 23, 'nationality': 'Italian', 'profession': 'bartender', 'hobbies' : ['pilates', 'jogging', 'painting'] }

print(Agnes['nationality'])
print(Agnes['profession'])
print(Agnes['hobbies'])

birthday = Agnes['age'] + 1
print(f"Agnes just turned {birthday}")

Agnes['x_position'] = 0
Agnes['y_position'] = 25
print(Agnes)

print(f'Original position: {Agnes['x_position']}')

#adding an element into the dictionary
Agnes['speed'] = 'normal'
#move agnes to the right
#determine the movement based on the speed
if Agnes['speed'] == 'slow':
	x_increment = 1
elif Agnes['speed'] == 'normal':
	x_increment = 2
else: #fast 
	x_increment = 3

Agnes['x_position'] = Agnes['x_position'] + x_increment

print(f'New position: {Agnes['x_position']}')

del Agnes['profession']
print(Agnes)