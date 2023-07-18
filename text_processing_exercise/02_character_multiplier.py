words_input = input().split()

first_word = words_input[0]
second_word = words_input[1]

sum = 0
index = 0

if len(first_word) > len(second_word):
    index = len(first_word)
else:
    index = len(second_word)

for i in range(index):
    if (len(first_word) - 1) < i <= (len(second_word) - 1):
        sum += ord(second_word[i])
    elif (len(first_word) - 1) >= i > (len(second_word) - 1):
        sum += ord(first_word[i])
    else:
        sum += ord(first_word[i]) * ord(second_word[i])

print(sum)
