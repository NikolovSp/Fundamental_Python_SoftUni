numbers = input().split()
sentence = input()

hidden_text = []
for num in numbers:
#     taken every number
    sum_digit = 0
    for digit in num:
        # print(digit, end=' ')
        sum_digit += int(digit)
    while sum_digit > len(sentence):
        sum_digit -= len(sentence)

    hidden_text.append(sentence[sum_digit])
    sentence = sentence[:sum_digit] + sentence[sum_digit + 1:]
    #make a new string omitting the value already used
    #print(sentence)
print(''.join(hidden_text))
