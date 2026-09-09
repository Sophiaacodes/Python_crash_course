responses = {}

#setting a flag to have an active poll
poll_active = True

while poll_active:
	#make the name and the response type
	name = input("\nWhat's ur name?: ")
	response = input("What's your favorite anime? ")

	#store response in dictionary
	responses[name] = response

	#find out if it goes on
	repeat = input("Is someone elses taking the poll? ")
	if repeat == 'no':
		poll_active = False

#show results
print("\n---Poll completed---")
for name, response in responses.items():
	print(f"\n{name.title()} likes {response.title()}")