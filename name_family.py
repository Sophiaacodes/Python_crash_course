#THE FAMILY I WAS BORN FROM
 #in this part I'm gonna study the list item, trying fixed and dynamic lists and also adding and removing items

#method 1 - build list is fixed
family_ages = ['1952', '1955', '2000', '2005']

Giorgio = f'my father was born in {family_ages[0]}'
Giovanna = f'my mother was born in {family_ages[1]}'
Sophiaa = f'I was born in {family_ages[2]}'
Paolo = f'my brother was born in {family_ages[-1]}'

message = f'{Giorgio.title()}, \n{Giovanna.title()}, \n{Sophiaa.title()}, \n{Paolo.title()}' 

print(message)

#method 2 - we made the build list dynamic 
family_ages = []

family_ages.append('1952')
family_ages.append('1955')
family_ages.append('2000')
family_ages.append('2005')

Giorgio = f'my father was born in {family_ages[0]}'
Giovanna = f'my mother was born in {family_ages[1]}'
Sophiaa = f'I was born in {family_ages[2]}'
Paolo = f'my brother was born in {family_ages[-1]}'

message = f'{Giorgio.title()}, \n{Giovanna.title()}, \n{Sophiaa.title()}, \n{Paolo.title()}' 

print(message)

#method 3 - we inset a new element
#Adding with the propriety .insert a new member to the family
family_ages.insert(2, '1999') #mind that what the number that you use with insert is the NUMBER THAT'S GONNA BE CHANGED

Giorgio = f'my father was born in {family_ages[0]}'
Giovanna = f'my mother was born in {family_ages[1]}'
Peemo = f'my boyfriend was born in {family_ages[2]}'
Sophiaa = f'I was born in {family_ages[3]}'
Paolo = f'my brother was born in {family_ages[-1]}'


message = f'{Giorgio.title()}, \n{Giovanna.title()}, \n{Peemo.title()}, \n{Sophiaa.title()}, \n{Paolo.title()}'

print(message)

#method 4 - we remove a few elements
#Removing with the propriety  so to conider that me and Peemo get married and we make out own family
del family_ages[0] #if you remove an elemet then you have to restart from [0] and you can't remove more than 1 element at the time
del family_ages[0]
del family_ages[-1]

Peemo = f'my husband was born in {family_ages[0]}' #then you each time reconsider as the list was shortened so in this case it would read family_ages = ['1999', '2000'] so Peemo becomes [0] and I [1]
Sophiaa = f'I was born in {family_ages[-1]}'

print(family_ages)

message = f'{Peemo.title()}, \n{Sophiaa.title()}, '

print(message)
