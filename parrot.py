prompt = "\nTell me something and i'll repeat it to you:"
prompt += "\nEnter 'quit' to end the program."

#FIRST VERSION 
'''
message = ""
while message != 'quit':
	message = input(prompt) #to make this work you can get there to the command prompt in the terminal, writing <C:User> cd C:User/.../python, then <C:User/.../python> python print.py and then your program will open
	
	if message != 'quit':
	print(message)
'''

#SECOND VERSION
#in this case we use a flag so that is cleaner
'''
active = True
while active:
	message = input(prompt)

	if message == 'quit': #the program is caps sensitive
		print("i'm so sorry to see u go!")
		active = False
	elif message == 'banana':
		print("You are a banana! I'm very intelligent and wait till i become a robot so i'll beat you up")
	else:
		print(message)
'''

#THIRD VERSION
#using break to exit the while loop
while True:
	message = input(prompt)

	if message == 'quit': 
		break
	elif message == 'banana':
		print("You are a banana! I'm very intelligent and wait till i become a robot so i'll beat you up")
	else:
		print(message)
