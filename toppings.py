requested_toppings = ['mushrooms', 'mozzarella', 'prosciutto']

if 'mushrooms' in requested_toppings:
	print('adding mushrooms')
if 'pepperoni' in requested_toppings:
	print('adding pepperoni')
if 'mozzarella' in requested_toppings:
	print('adding mozzarella')

print("\nhere's ur pizza!")

#using elif blocks the code from running when one test passes
if 'mushrooms' in requested_toppings:
	print('\nadding mushrooms')
elif 'pepperoni' in requested_toppings:
	print('adding pepperoni')
elif 'mozzarella' in requested_toppings:
	print('adding mozzarella')

print("\nhere's ur pizza!")

#tying to use a for loop also
for requested_topping in requested_toppings:
	if requested_topping == 'mozzarella' :
		print(f"Sorry we're out of {requested_topping}.") #this is contestual on where the item is positioned in the list
	else :
		print(f"Adding now {requested_topping}.")

print ("your pizza is ready!")

for requested_topping in requested_toppings:
	if requested_topping == 'prosciutto' :
		requested_toppings.remove('prosciutto') #not really necessary, it was just to remember how to use .remove
		print(requested_toppings)
		print(f"Sorry we're out of {requested_topping}. the only thing we can add are {requested_toppings}") #this is contestual on where the item is positioned in the list
	else :
		print(f"Adding now {requested_topping}.")

print ("your pizza is ready!")

#prompting the client on an empty list
requested_toppings= []

if requested_toppings :
	for requested_topping in requested_toppings :
		print( f"Adding {requested_topping}")
	print("\nFinishing your pizza right now.")
else :
	print("Want to add some toppings?")

available_toppings = ['mushrooms', 'prosciutto', 'tuna', 'onion', 'mozzarella']

requested_toppings = ['olives', 'tuna', 'onion']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else: 
		print(f"Sorry, we don't have {requested_topping}.")
print(f"\n Finishing your pizza")