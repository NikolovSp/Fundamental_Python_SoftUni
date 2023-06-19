numbers = input().split()

even_numbers = lambda x: int(x) % 2 == 0

ordered = list(filter(even_numbers, numbers))
ordered = [int(x) for x in ordered]
print(ordered)
