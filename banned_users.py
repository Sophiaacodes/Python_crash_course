banned_users = ['maria', 'giulia', 'christian']
user_one = 'diana'
user_two = 'maria'

#NORMAL IF STATEMENTS
if user_one not in banned_users:
	print (f'{user_one.title()} is not banned')
	print (f'you can now respond')

if user_two not in banned_users : #if the test does not pass the entire block of lines will be ignored
	print (f'\n{user_two.title()} is banned')
	print (f'you can now respond')

if user_two in banned_users :
	print (f'\n{user_two.title()} is banned')
	print (f'you are banned')

#IF ELSE STATEMENTS
if user_two not in banned_users:
	print(f'\n{user_two.title()}, you can write')
else :
	print(f'\n{user_two.title()}, you cannot write, uou are banned')

banned_users.remove ('maria') #let's unban maria

if user_two not in banned_users:
	print(f'\n{user_two.title()}, you can write')
else :
	print(f'\n{user_two.title()}, you cannot write, uou are banned')