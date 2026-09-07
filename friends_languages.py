favorite_languages = {
	'olly': 'javascript',
	'niky': 'ruby',
	'diletta': 'python',
	'erika': 'javascript'
}

friends = ['niky', 'diletta']
for name in favorite_languages.keys(): #tells that it has to extract from the dictionary all the keys and give each of them one at the time the variable name
	print(name.title())#this prints all names 

	if name in friends:
		print(name.title())#this gets to print just the name in friends
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

#let's try with get()
favorite_language = favorite_languages.get('erin', 'Erin, please take our poll!')
print(favorite_language)

#let's try deleting and addind items
del favorite_languages['olly']
print(favorite_languages)

favorite_languages['olly'] = 'javascript'
print(favorite_languages)

for name in sorted(favorite_languages.keys()):
	print(f'{name.title()}, thank you for taking the poll.')

#let's look at the values withouth the keys
print('the following languages have been mentioned:')
for language in favorite_languages.values():
	print(language.title())

#let's see what's popular
print('the following languages have been mentioned:')
for language in set(favorite_languages.values()): #since javascript was mentioned twice it does not repeat the term
	print(language.title())