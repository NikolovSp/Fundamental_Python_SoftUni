def characters_in_ascii(a, b):

    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=' ')



char_a = input()
char_b = input()
characters_in_ascii(char_a, char_b)

# print(ord(char_a))
# print(ord(char_b))