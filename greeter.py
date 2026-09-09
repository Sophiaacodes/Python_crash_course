def get_formatted_name(first_name, last_name):
	full_name = f'{first_name} {last_name}'
	return full_name.title()

#this is an infinite loop!
while True:
	print("\nPlease enter your name:")
	print("(enter 'q' to quit instead)")

	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}")

	break
