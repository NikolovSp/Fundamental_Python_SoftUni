items = input().split('|')
budget = float(input())
profit = 0
new_prices = []
# print(items)
for order in items:
    order_list = order.split('->')
    item = order_list[0]
    price = float(order_list[1])
    # print(item)
    # print(price)
    if item == "Clothes":
        if price > 50.00:
            continue
    elif item == "Shoes":
        if price > 35.00:
            continue
    elif item == "Accessories":
        if price > 20.50:
            continue
    #reduce the price depending on item if enought budget available
    if budget >= price:
        budget -= price
        profit += price * 0.4
        new_prices.append(price * 1.4)
    else:
        continue

budget = budget + sum(new_prices)
for price in new_prices:
    print(f'{price:.2f}', end=' ')
# not sure how to format printing of list with 2 digits or how to remove brackets/commas
print()
print(f'Profit: {profit:.2f}')
if budget > 150:
    print('Hello, France!')
else:
    print('Not enough money.')
