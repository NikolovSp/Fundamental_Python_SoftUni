# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy
orders = {}
while True:
    command = input()
    if command == 'buy':
        break
    name, price, quantity = command.split()
    price = float(price)
    quantity = float(quantity)

    if name not in orders:
        orders[name] = {}
    orders[name] = price, quantity

# {'Beer': [2.2, 100.0], 'IceTea': [1.5, 50.0], 'NukaCola': [3.3, 80.0], 'Water': [1.0, 500.0]}
# dictionary with price and quantity as list values

# for key, value in orders.items():
#     print(f"{key} -> {value[0] * value[1]:.2f}")

print(orders)
