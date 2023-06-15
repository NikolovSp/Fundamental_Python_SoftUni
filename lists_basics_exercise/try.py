level_of_fire = input().split('#')
# water_available = int(input())
# print(level_of_fire)
effort = 0
cells_put_out = []
for fire in level_of_fire:
    cell_fire = fire.split(' = ')
    type_of_fire = cell_fire[0]
    energy_of_fire = int(cell_fire[1])
    # print(type_of_fire)
    # print(energy_of_fire)

    if type_of_fire == 'High':
        if energy_of_fire < 80 or energy_of_fire > 125:
            continue
    elif type_of_fire == 'Medium':
        if energy_of_fire < 50 or energy_of_fire > 80:
            continue
    elif type_of_fire == 'Low':
        if energy_of_fire < 1 or energy_of_fire > 50:
            continue
