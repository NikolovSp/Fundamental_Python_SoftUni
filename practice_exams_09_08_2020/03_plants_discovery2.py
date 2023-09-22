n = int(input())
plants_start = {}

for i in range(n):
    plant, rarity = input().split('<->')
    plants_start[plant] = [int(rarity)]

print(plants_start)

while True:
    command = input()
    if command == 'Exhibition':
        break

    activity, rest = command.split(': ')

    if activity == 'Reset':
        plants_start[rest][1] = 0.00

    plant, rating = rest.split(' - ')

    if plant not in plants_start.keys():
        print('error')
        continue

    if activity == 'Rate':


    if activity == 'Update':
        plants_start[plant][0] = int(rating)

print(plants_start)