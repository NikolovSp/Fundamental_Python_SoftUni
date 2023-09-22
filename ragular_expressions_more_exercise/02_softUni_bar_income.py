import re
pattern = r'%([A-Z][a-z]+)%<([\w]+)>\|(\d)\|(\d+\.?\d+)\$'
order = input()
total_income = 0
while order != 'end of shift':
    match = re.search(pattern, order)

    if match:
        customer_name, product, count, price = match.groups()
        total_price = int(count) * float(price)
        print(f"{customer_name}: {product} - {total_price:.2f}")
        total_income += total_price
    order = input()

print(f'Total income: {total_income:.2f}')
