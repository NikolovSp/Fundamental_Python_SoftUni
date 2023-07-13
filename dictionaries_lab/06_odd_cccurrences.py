command = input().split()
# print(command)
my_dict = {}
for word in command:
    word = word.lower()
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

for k, v in my_dict.items():
    if v % 2 != 0:
        print(k, end=' ')
# print(my_dict)
