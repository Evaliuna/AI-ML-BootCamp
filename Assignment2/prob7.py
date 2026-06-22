"""
i took input from user senctence and the searching word. then used if in to check
is the word in the sentence and printed out yes or no.
"""
sentence = input("Enter a sentence: ")
word = input("Enter the word to search for: ")

if word in sentence:
    print(f"Yes, '{word}' is present inside the sentence.")
else:
    print(f"No, '{word}' is not present inside the sentence.")