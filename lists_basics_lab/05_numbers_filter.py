n = int(input())

current_list = [int(input()) for num in range(n)]
filtered_list = []
command = input()

if command == 'even':
    for num in current_list:
        if num % 2 == 0:
            filtered_list.append(num)
if command == 'odd':
    for num in current_list:
        if num % 2 != 0:
            filtered_list.append(num)
if command == 'positive':
    for num in current_list:
        if num >= 0:
            filtered_list.append(num)
if command == 'negative':
    for num in current_list:
        if num < 0:
            filtered_list.append(num)
print(filtered_list)
