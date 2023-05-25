quantity = int(input())
days_until_christmas = int(input())

total_cost = 0
total_spirit = 0

ORNAMENT_SET_PRICE = 2
ORNAMENT_SET_SPIRIT = 5

TREE_SKIRT_PRICE = 5
TREE_SKIRT_SPIRIT = 3

TREE_GARLAND_PRICE = 3
TREE_GARLAND_SPIRIT = 10

TREE_LIGHTS_PRICE = 15
TREE_LIGHTS_SPIRIT = 17


for day in range(1, days_until_christmas + 1):

    if day % 11 == 0:
        quantity += 2

    if day % 10 == 0:
        total_spirit -= 20
        total_cost += (TREE_GARLAND_PRICE + TREE_SKIRT_PRICE + TREE_LIGHTS_PRICE)

        if day == days_until_christmas:
            total_spirit -= 30

    if day % 2 == 0:
        total_cost += ORNAMENT_SET_PRICE * quantity
        total_spirit += ORNAMENT_SET_SPIRIT

    if day % 3 == 0:
        total_cost += (TREE_SKIRT_PRICE + TREE_GARLAND_PRICE) * quantity
        total_spirit += (TREE_SKIRT_SPIRIT + TREE_GARLAND_SPIRIT)

    if day % 5 == 0:
        total_cost += TREE_LIGHTS_PRICE * quantity
        total_spirit += TREE_LIGHTS_SPIRIT

    if day % 15 == 0:
        total_spirit += 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit}')
