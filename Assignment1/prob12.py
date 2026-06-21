text = 'Data, Science, Machine, Learning'

text_list = text.split(',')
print("List:", text_list)

print("Second elelment:", text_list[1])
print("Total number of elements:", len(text_list))
joined_text = ' -> '.join(text_list)
print("Joined string:", joined_text)