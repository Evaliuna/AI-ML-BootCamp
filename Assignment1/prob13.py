"""
i toke the given sentence then used string slicing.
first to print 1st 5 character then used - to print back or last 6 character
then used :: to go through the whole sentence print one word then skip 2 continue like this.
finally -1 means start from backward one by one print each character.
"""

sentence = 'Hello World Python'

print("First 5 characters:", sentence[:5])
print("Last 6 characters:", sentence[-6:])
print("Every second character:", sentence[::2])
print("Entire string reversed:", sentence[::-1])