first_line = input().split(', ')
second_line = input().split(', ')

new_list = []

for char in range(len(first_line)):
    for i in range(len(second_line)):
        if first_line[char] in second_line[i]:
            if first_line[char] not in new_list:
                new_list.append(first_line[char])

print(new_list)
