"""
I implemented the given string then i split it into a list by ',' and print it also print out second element also to find 
the total number of elements i use len() and finally to connect the list element using'->' i used .join(list name).
"""
text = 'Data, Science, Machine, Learning'
text_list = text.split(',')
print("List:", text_list)

print("Second elelment:", text_list[1])
print("Total number of elements:", len(text_list))
joined_txt = ' -> '.join(text_list)
print("Joined string:", joined_txt)