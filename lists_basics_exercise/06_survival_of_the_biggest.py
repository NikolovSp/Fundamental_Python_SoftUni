numbers = input().split()
numbers_remove = int(input())

numbers_list = [int(x) for x in numbers]

for min_remove in range(numbers_remove):
    numbers_list.remove(min(numbers_list))

print(*numbers_list, sep=', ')
