prompt = "\ntell me something and i'll repeat it to you: "
prompt += "\nenter 'quit' to end the program"

message = ""
while message != 'quit':
	message = input(prompt) #to make this work you can get there to the command prompt in the terminal, writing <C:User> cd C:User\...\python, then <C:User\...\python> python print.py and then your program will open
	
	if message != 'quit':
	print(message)