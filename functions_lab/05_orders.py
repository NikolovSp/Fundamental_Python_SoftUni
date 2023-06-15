def order_price(product, n):
    if product == 'coffee':
        return f'{n * 1.50:.2f}'
    elif product == 'water':
        return f'{n * 1.00:.2f}'
    elif product == 'coke':
        return f'{n * 1.40:.2f}'
    elif product == 'snacks':
        return f'{n * 2.00:.2f}'


order_product = input()
quantity = int(input())
print(order_price(order_product, quantity))

