number = list(map(int, input().split(', ')))
even_numbers = map(lambda x: x if number[x] % 2 == 0 else 'no', range(len(number)))
even_index = list(filter(lambda x: x != 'no', even_numbers))
print(even_index)
