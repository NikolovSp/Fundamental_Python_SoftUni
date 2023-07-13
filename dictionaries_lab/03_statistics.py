bakery = {}
while True:
    food = input()
    if food == 'statistics':
        break

    product, quantity = food.split(': ')
    quantity = int(quantity)
    if product in bakery:
        bakery[product] += quantity
    else:
        bakery[product] = quantity

print("Products in stock:")
for k, v in bakery.items():
    print(f"- {k}: {v}")
print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")
