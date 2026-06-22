word = 'Banana'

print("find('a'):", word.find('a')) #it checks if we can find letter a and print the first position it found.
print("count('a'):", word.count('a')) #it counts how many a is in the word
print("startswith('Ba'):", word.startswith('Ba')) #it checks if it starts with Ba or not
print("endswith('na'):", word.endswith('na')) #same it checks if the word ends with na or not
print("Is 'Banana' a digit?:", word.isdigit()) #it checks if the word is digit or not
print("Is '12345' a digit?:", '12345'.isdigit()) #it checks if the given string is digit or not
print("Is '123a5' a digit?:", '123a5'.isdigit()) #it gives false because it has a character on the string so it"s not entirely digit
