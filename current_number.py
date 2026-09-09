'''current_number = 2
while current_number <= 5:
	print(current_number)
	current_number += 1'''

#counting only odd numbers
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0: #it checks that if it can be devided by 2 it starts back the loop from the beginning so ti doesn't print even numbers
		continue

	print(current_number)

