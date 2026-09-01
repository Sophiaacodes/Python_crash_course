#page 40 chap 3 for stack concept
#WORKING ON THE .pop() METHOD
 #with this method you can delete the element of the list and still REUSE IT as you please, if you don't want to reuse it use the del statement
subjects = ['chemistry', 'math','cs']

print(subjects)

#DELETING THE FIRST ITEM OF THE STACK - LAST OF THE LIST
already_studied_subjects = subjects.pop()

print(subjects)
 # U cannot print(subjects.title()) cuz AttributeError: 'list' object has no attribute 'title'

print(already_studied_subjects)
print(already_studied_subjects.title())
 # U can print tho print(already_studied_subjects.title()), cuz that's just a value so U can use it like:

print(f"I have already studied {already_studied_subjects.upper()} during the summer.")

#DELETING THE LAST ITEM OF THE STACK - FIRST OF THE LIST
not_studied_in_years = subjects.pop(0)

print(subjects)

print(not_studied_in_years)
print(not_studied_in_years.upper())

print(f"but unfurtunately I have not studied {not_studied_in_years.title()} in years.")

