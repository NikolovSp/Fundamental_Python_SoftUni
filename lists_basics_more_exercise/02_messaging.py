numbers = input().split(' ')
text = [input()]
print(text)

# numbers = [int(x) for x in numbers]
new_text = []
for num in numbers:
    index = 0
    for char in num:
        char = int(char)
        index += char
    if index >= len(text):
        index = index - len(text)
    new_text.append(text[index])
    text.remove(index)
print(*new_text, sep='')

