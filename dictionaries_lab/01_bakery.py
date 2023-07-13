groceries = input().split()
bakery = {}

for i in range(0, len(groceries), 2):
    food = groceries[i]
    quantity = groceries[i + 1]
    bakery[food] = int(quantity)

print(bakery)
