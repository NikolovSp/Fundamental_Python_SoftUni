key = int(input())
lines = int(input())
encrypted = []
for line in range(lines):
    letter = input()
    new_letter = ord(letter) + key
    encrypted.append(chr(new_letter))
print(*encrypted, sep='')


