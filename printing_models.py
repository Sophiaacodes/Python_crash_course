unprinted_designs = ['phone case', 'robot pendant', 'rubik cube']
completed_models = []

#simulate printing each design
#moving completed_design after printing
while unprinted_designs:
	printing_design = unprinted_designs.pop()
	print(f"Printing model: {printing_design}")
	completed_models.append(printing_design)

#displaying completed models 
completed_models.sort()
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

#SAME THING USING def function
def print_models(unprinted_designs, completed_models):
	'''
	Simulate each design printing untile none is left
	Move design to completed_models
	'''

	while unprinted_designs:
		printing_design = unprinted_designs.pop()
		print(f"Printing model: {printing_design}")
		completed_models.append(printing_design)
		completed_models.sort()

def show_completed_models(completed_models):
	'''Showing printed models'''
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['robot pendant', 'phone case', 'rubik cube']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print(unprinted_designs) #the list is empty
