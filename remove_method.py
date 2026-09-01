#the remove method allows you to remove an item without knowing it's position on the list

subjects = ['math', 'CHEMISTRY', 'CS', 'phisics']

print(subjects)

#using just the remove directly
subjects.remove('CHEMISTRY')
print(subjects)

#using remove as part of a value
subjects_not_studied = 'CHEMISTRY'

#the if function grants that there's no error, confirming that the element is not present already in the list
if subjects_not_studied in subjects:
    subjects.remove(subjects_not_studied)
else:
    print(f"the element'{subjects_not_studied}' was already removed.")

print(subjects)
print(f'\nI have not studied {subjects_not_studied.lower()} in four years') 
#is the result defined by the variable subject_not_studied , but not of the element of the list, since it was already deleted by line 8