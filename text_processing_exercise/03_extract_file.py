path = input()

path = path.partition('.')
extension = path[2]
rest = path[0].split('\\')

print(f'File name: {rest[-1]}')
print(f'File extension: {extension}')

# list_text = input().split("\\")
# new_list = list_text[-1].split(".")
#
# print(f"File name: {new_list[0]}")
# print(f"File extension: {new_list[1]}")