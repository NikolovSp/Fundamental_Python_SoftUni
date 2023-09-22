heroes = {}
number_heroes = int(input())

for i in range(number_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = [hit_points, mana_points]
print(heroes)

while True:
    command = input().split(' - ')

    print(command)
    if command[0] == 'End':
        break
    if len(command) == 3:
        current_hero_name = command[1]
        amount = int(command[2])

        if command[0] == 'Heal':
            previous_health = heroes[current_hero_name][1]
            amount_received = amount
            heroes[current_hero_name][1] += amount
            if heroes[current_hero_name][1] > 100:
                heroes[current_hero_name][1] = 100
                amount_received = 100 - previous_health
            print(f"{current_hero_name} healed for {amount_received} HP!")

        elif command[0] == 'Recharge':
            previous_MP = heroes[current_hero_name][2]
            amount_recovered = amount
            heroes[current_hero_name][2] += amount
            if heroes[current_hero_name][2] > 200:
                heroes[current_hero_name][2] = 200
                amount_recovered = 200 - previous_MP
            print(f"{current_hero_name} recharged for {amount_recovered} MP!")

    elif len(command[0]) == 4:
        if command[0] == 'CastSpell':
            current_hero_name = command[1]
            MP_needed = int(command[2])
            spell_name = command[3]

            if heroes[current_hero_name][2] >= MP_needed:
                MP_left = heroes[current_hero_name][2] - MP_needed
                heroes[current_hero_name][2] = MP_left
                print(f"{current_hero_name} has successfully cast {spell_name} and now has {MP_left} MP!")
            else:
                print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")

        elif command[0] == 'TakeDamage':
            current_hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]

            if heroes[current_hero_name][1] > damage:
                current_HP = heroes[current_hero_name][1] - damage
                heroes[current_hero_name][1] = current_HP
                print(f"{current_hero_name} was hit for {damage} HP by {attacker} and now has {current_HP} HP left!")
            else:
                print(f"{current_hero_name} has been killed by {attacker}!")
                del heroes[current_hero_name]

for hero in heroes.keys():
    print(hero)
    # for i in range(len(heroes[hero])):
    #     print(f'HP: {}')




