letters = input()
capitals = []
counter = 0
for element in letters:
    if element.isupper():
        capitals.append(counter)
    counter += 1
print(capitals)

