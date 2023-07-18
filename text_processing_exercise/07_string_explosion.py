explosion = input()
# result = ''
# for index in range(len(explosion)):
#     if explosion[index] == '>':
#         delete = int(explosion[index + 1])
#         for j in range(1, delete + 1):
#             explosion = explosion.replace(explosion[index + j], '')
# print(explosion)

for index in range(len(explosion) -1, 0, -1):
    if explosion[index] == '>':
        delete = int(explosion[index + 1])
        for j in range(1, delete + 1):
            explosion = explosion.replace(explosion[index], '')
print(explosion)
