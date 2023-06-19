number = input()
numbers = [int(x) for x in number]
numbers.sort(reverse=True)

print(*numbers, sep='')
