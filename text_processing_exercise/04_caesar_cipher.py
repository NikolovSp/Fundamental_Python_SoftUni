code_to_cypher = input()
ciphered_code = [chr(ord(char) + 3) for char in code_to_cypher]
print(''.join(ciphered_code))

# code_to_cypher = input()
# # ciphered_code = [ for char in code_to_cypher]
# ciphered_code = ''
# for char in code_to_cypher:
#     ciphered_code += (chr(ord(char) + 3))
#     # ciphered_code += chr(ord([char]) + 3)
# print(ciphered_code)
