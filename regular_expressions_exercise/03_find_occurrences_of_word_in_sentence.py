# words = [word.lower() for word in input().split()]
# key_word = input()
# counter = 0
# for word in words:
#     if key_word == word:
#         counter += 1
#
# print(counter)

import re

sentence = input()
key_word = input()

pattern = fr'\b{key_word}\b'
# fr'(?i)\b{key_word}\b' another wat to ignore case

match = re.findall(pattern, sentence, re.IGNORECASE)

print(len(match))
