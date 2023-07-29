# explosion = input()
# # result = ''
# # for index in range(len(explosion)):
# #     if explosion[index] == '>':
# #         delete = int(explosion[index + 1])
# #         for j in range(1, delete + 1):
# #             explosion = explosion.replace(explosion[index + j], '')
# # print(explosion)
#
# for index in range(len(explosion) -1, 0, -1):
#     if explosion[index] == '>':
#         delete = int(explosion[index + 1])
#         for j in range(1, delete + 1):
#             explosion = explosion.replace(explosion[index], '')
# print(explosion)

some_string = input()
explosion = 0
final = ''

for index in range(len(some_string)):
    if explosion > 0 and some_string[index] != ">":
        explosion -= 1
    elif some_string[index] == ">":
        final += some_string[index]
        explosion += int(some_string[index + 1])
    else:
        final += some_string[index]
print(final)
