lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expense = 0
shield_counter = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        total_expense += helmet_price
    if fight % 3 == 0:
        total_expense += sword_price

    if fight % 2 == 0 and fight % 3 == 0:
        total_expense += shield_price
        shield_counter += 1

        if shield_counter % 2 == 0:
            total_expense += armor_price
print(f'Gladiator expenses: {total_expense:.2f} aureus')
