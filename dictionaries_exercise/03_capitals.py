countries = input().split(', ')
capitals = input().split(', ')

# world = {}
# for i in range(len(countries)):
#     world[countries[i]] = capitals[i]
#
# # print(world)
# for k, v in world.items():
#     print(f'{k} -> {v}')


for i, ch in zip(countries, capitals):
    print(f"{i} -> {ch}")
