import re
furniture_list = []
total_price = 0
# pattern = r'>>([A-Za-z]+)<<([1-9]+[0-9\.]+)!([1-9])'
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

while True:
    command = input()

    if command == 'Purchase':
        break

    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        price = float(price)
        quantity = int(quantity)
        furniture_list.append(furniture)

        # furniture.append(match.group(1))
        # price = float(match.group(2))
        # quantity = int(match.group(3))
        total_price += price * quantity

print('Bought furniture:')
for furniture in furniture_list:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
