count = int(input())
factor = int(input())

new_list = []

for x in range(1, factor + 1):
    num = count * x
    new_list.append(num)

print(new_list)
