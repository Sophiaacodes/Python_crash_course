#looping trought a list

subjects = ['math', 'CHEMISTRY', 'CS', 'physics']

for subject in subjects :
     print(subject)

#you can still modify the order of the elements in the list and then do loop
subjects.sort(reverse=True) #alphabetical reversed order
for subject in subjects:
    print(subject)


for subject in subjects :
    print(f"I'm gonna get a 30L/30 in {subject.title()}")
    print(f"{subject.title()}, is gonna come easy to me")
    print(f'everything comes easy to me, especially {subject.title()}\n') #one for each element cuz indented

print(f'everything comes easy to me, especially {subject.title()}')#only last element cuz not indented