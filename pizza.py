def make_pizza(size, *toppings): #you can add as many toppings you want cuz of the * 
	print(f"\nRequested a {size} inch pizza with:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(15,'pepperoni')
make_pizza(16,'mushroom', 'prosciutto', 'provola')


def make_pizza(size, sauce, **pizza_component):
	'''building a dictionary for the pizza place'''
	pizza_component['size_of_pizza'] = size
	pizza_component['sauce_on_pizza'] = sauce
	return pizza_component

pizza = make_pizza('16-inch', 'pesto', extra_topping_1 = 'burrata', extra_topping_2 = 'prosciutto')
print(pizza)