sentence = input("Enter a sentence: ")
word = input("Enter the word to search for: ")

if word in sentence:
    print(f"Yes, '{word}' is present inside the sentence.")
else:
    print(f"No, '{word}' is not present inside the sentence.")