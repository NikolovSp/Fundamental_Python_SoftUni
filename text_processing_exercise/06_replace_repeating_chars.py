# letters = [str(char) for char in input()]
letters = input()
new_letters = ''
previous_char = None

for char in letters:
    if char != previous_char:
        new_letters += char
    previous_char = char
print(new_letters)
