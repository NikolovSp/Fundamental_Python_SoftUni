orders = {}
while True:
    command = input()
    if command == 'buy':
        break
    name, price, quantity = command.split()
    price = float(price)
    quantity = float(quantity)

    if name not in orders.keys():
        orders[name] = [price, quantity]
    else:
        orders[name][0] = price
        orders[name][1] += quantity

# {'Beer': [2.2, 100.0], 'IceTea': [1.5, 50.0], 'NukaCola': [3.3, 80.0], 'Water': [1.0, 500.0]}
# dictionary with price and quantity as list values

for product, value in orders.items():
    print(f"{product} -> {value[0] * value[1]:.2f}")
