# now the users are not confirmed
unconfirmed_users = ['alice', 'anna', 'cecilia', 'joice', 'anna', 'lola', 'agnes', 'anna']
confirmed_users = []

#removing anna
while 'anna' in unconfirmed_users:
	unconfirmed_users.remove('anna')

#sorting in alphabetical order (reversed cuz we are using pop after)
unconfirmed_users.sort(reverse=True)

#verify until unconfirmed_users is empty
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print(f"verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

#display all confirmed users
print("\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(f"{confirmed_user.title()} has been confirmed")