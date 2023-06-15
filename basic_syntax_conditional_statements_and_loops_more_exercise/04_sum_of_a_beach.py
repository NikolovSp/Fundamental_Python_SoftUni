summer = input().lower()
needed_words = ['sand', 'water', 'fish', 'sun']
counter = 0
for char in needed_words:
    while char in summer:
        counter += 1
        summer = summer.replace(char, '', 1)


print(counter)
