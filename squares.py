squares = []
for value in range(1,11):
	square = value ** 2 #the ** means exponents
	squares.append(square)

print(squares)

three_times = []
for value in range(1,11):
	third_time = value ** 3
	three_times.append(third_time) #the append method is the one that adds element to the end of the list
	#so basically we re telling the program that you have to add the element third_time in the list, made by looping between 1 and 10 and taking each number and making it **3

print(three_times)

#MORE CONCISE VERSION
squares = []
for value in range(1,11):
	squares.append(value ** 2)

print(squares)

#LIST COMPREHENSION VERSION
squares = [value**2 for value in range (1,11)]
print(squares)

#trying to apply what i've learned
pages_to_study = list(range(1,43))
days_left = list(range(1,21))
print(f'I need to study {pages_to_study[-1]/days_left[-1]} pages each day')
