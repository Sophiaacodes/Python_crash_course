#the remove method allows you to remove an item without knowing it's position on the list

subjects = ['math', 'CHEMISTRY', 'CS', 'phisics']

print(subjects)

#using just the remove directly
subjects.remove('CHEMISTRY')
print(subjects)

#using insert to add the subject into position 0
subjects.insert(3,'CHEMISTRY')
print(subjects)

#SORTING out the list into alphabetical order
subjects.sort()
print(subjects)

#sorting alphabetically but upside down 
subjects.sort(reverse=True)
print(subjects)

#changing subjects manually to it's original form
subjects = ['math', 'CHEMISTRY', 'CS', 'phisics']

print(f"\nHere's the original list: \n{subjects}")

print(f"\nHere's the sorted list: \n{sorted(subjects)}") 
#in a function you need to use between{} what you0d write if it was written inside print()

print(f"\nHere's the sorted reversed list: \n{sorted(subjects, reverse=True)}") #use the comma if 2+ elements in the same()

print(f"\nHere's the original lit again: \n{subjects}")

#reversing permanently
print(subjects)

subjects.reverse() #this just reverses the order, it's not like doing .sort(reverese=True)
print(subjects)

print(subjects) #it is indeed reversed permanently

subjects.reverse() #to reverse it you need to reuse the .reverse() function
print(subjects)
