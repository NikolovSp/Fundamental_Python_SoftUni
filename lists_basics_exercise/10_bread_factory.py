events = input().split('|')
COINS = 100
ENERGY = 100
bakery_open = True

for event in events:
    activity = event.split('-')
    action = activity[0]
    price = int(activity[1])

    if action == 'rest':
        current_energy = ENERGY
        ENERGY += price
        if ENERGY > 100:
            ENERGY = 100
        print(f"You gained {ENERGY - current_energy} energy.")
        print(f"Current energy: {ENERGY}.")

    elif action == 'order':
        current_energy = ENERGY
        ENERGY -= 30
        if ENERGY < 0:
            ENERGY = current_energy + 50
            print(f'You had to rest!')
        else:
            COINS += price
            print(f'You earned {price} coins.')

    else:
        COINS -= price
        if COINS < 0:
            print(f'Closed! Cannot afford {action}.')
            bakery_open = False
            break
        else:
            print(f'You bought {action}.')

if bakery_open:
    print('Day completed!')
    print(f'Coins: {COINS}')
    print(f"Energy: {ENERGY}")
