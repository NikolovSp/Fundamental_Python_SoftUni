animals = input().split(', ')

# for index in range(len(animals) - 1, -1, -1):
if animals[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
    exit()

for index in range(len(animals) - 1):
    if animals[index] == 'wolf':
        print(f'Oi! Sheep number {len(animals) - (index + 1)}! You are about to be eaten by a wolf!')

