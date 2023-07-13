letters = input()
chars_count = {}

for char in letters:
    if char == ' ':
        continue
    if char not in chars_count:
        chars_count[char] = 0
    chars_count[char] += 1

for k, v in chars_count.items():
    print(f'{k} -> {v}')
