def ascii_sum_char(first_word, second_word):
    num = 0
    sum = 0
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
    return sum

words_input = input().split()

first_word = words_input[0]
second_word = words_input[1]
print(ascii_sum_char(first_word, second_word))
