#the concept is entering in a museum:
#if u are under 5 the ticket is 0€
#if u are between 5 and 18 the ticket is 3€
#if u are above 18 the ticket is 10€

age = 15

if age < 5 :
	print (f'Your ticket is 0€. \nYou can now enter for free')
elif age < 18 : #you can just write elif and it will exclude the < 5 age group
	print (f'You have youth reduction. \nYour ticket is now 3€')
else :
	print (f'You have to pay full price. \nIt will be 10€')

#more coincise version
age = 60

if age  < 5 :
	price = 0
elif age < 18 :
	price = 3
elif age < 65 :
	price = 10
else : #can include invalid or malicious data cuz matches any condition that was not matched by a specific if or elif
	price = 5

print (f'The fee for the entrance at the museum for you would be €{price}.')

age = 66

if age  <5 :
	price = 0
elif age < 18 :
	price = 3
elif age < 65 :
	price = 10
elif age >= 65: #in this way the block of code has to have a specific order to execute
	price = 5

print (f'The fee for the entrance at the museum for you would be €{price}.')