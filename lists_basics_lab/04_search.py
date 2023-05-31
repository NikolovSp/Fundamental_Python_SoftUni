n = int(input())
word = input()

start_list = [input() for string in range(n)]
print(start_list)

new_list = []
for string in start_list:
    if word in string:
        new_list.append(string)
print(new_list)
