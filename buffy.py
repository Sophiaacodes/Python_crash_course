#working on the first list
buffy_vampire_slayer = ['buffy', 'willow', 'angel', 'xander', 'cordelia', 'drusilla','spike']
#copying the list
humans_vs_vamps = buffy_vampire_slayer[:] #if i were to write just humans_vs_vamps = buffy_vampire_slayer it would associate the two lists and i wouldn't get to change the humans_vs_vamps list

#messages i can do using the first list
message = f'Here are the good people:'
print(message)

for good in buffy_vampire_slayer[:5]:
	print(good.title())

message = f'\nThese are the bad people:'
print(message)
for bad in buffy_vampire_slayer[-2:]:
	print(bad.title())

relations_one = f"{buffy_vampire_slayer[0].title()} is {buffy_vampire_slayer[2].title()}'s girlfriend"
relations_two = f"{buffy_vampire_slayer[4].title()} is {buffy_vampire_slayer[3].title()}'s girlfriend"
relations_three = f"{buffy_vampire_slayer[-2].title()} is {buffy_vampire_slayer[-1].title()}'s girlfriend"
print(f'\n{relations_one}, \n{relations_two}, \n{relations_three}.')#this way i can make order in what i write using \n

#edits to the second list
del humans_vs_vamps[2]
humans_vs_vamps.insert(4, 'angel') 

#messages i can do using the second list
for humans in humans_vs_vamps[:4]:
	message = f'\n{humans.title()} is a human'
	print(message)

for vamps in humans_vs_vamps [-3:]:
	message = f'\n{vamps.title()} is a vampire,'
	print(message)à


sire_one = f"{humans_vs_vamps[4].title()} is {humans_vs_vamps[5].title()}'s sire"
sire_two = f"{humans_vs_vamps[5].title()} is {humans_vs_vamps[6].title()}'s sire"
print(f'\n{sire_one}, \n{sire_two}.')

