my_dict = {'name': 'Gosho', 'age': 35, 'school': 'Student', 'key': 'Value', 'education': "Master's", 'friends': 10}

print(my_dict['name'])
my_dict['age'] += 5
print(my_dict['age'])
my_dict['key'] = 'Question'
print(my_dict['key'])

print(my_dict.items())

print(my_dict.keys())

print(my_dict.values())

print(my_dict.pop('key')) # returns the value of a key in the dictionary and removes it from the dict.
