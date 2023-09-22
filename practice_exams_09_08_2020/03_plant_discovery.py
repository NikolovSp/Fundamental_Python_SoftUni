number_of_lines = int(input())
plants = {}
for information in range(number_of_lines):
    plant, rarity = input().split("<->")
    plants[plant] = [int(rarity), 0]
print(plants)

command = input()

while command != 'Exhibition':

    command = command.split(': ')
    activity = command[0]


    # if plant not in plants:
    #     print('error')
    #     continue

    if activity == 'Rate':
        current_plant, rating = command[1].split(' - ')
        plants[current_plant][1] += int(rating) / 2

    if activity == 'Update':
        current_plant, new_rarity = command[1].split(' - ')
        plants[current_plant][0] = int(new_rarity)

    if activity == 'Reset':
       current_plant = command[1]
       del plants[current_plant][1]

print(plants)
