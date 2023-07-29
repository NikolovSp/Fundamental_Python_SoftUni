import re

regex = r'\d+'
while True:
    text = input()
    if len(text) == 0:
        break
    matches = re.findall(regex, text)
    if len(matches) > 0:
        print(*matches, end=' ')
