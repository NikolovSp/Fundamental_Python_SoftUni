numbers = input().split(', ')
numbers = [int(n) for n in numbers]
# print(numbers)
for item in numbers:
    if item == 0:
        numbers.append(item)
        numbers.remove(item)
print(numbers)
