lst = []
for i in range(3):
    command = input()
    lst.append(command)

lst[0], lst[2] = lst[2], lst[0]

print(lst)
