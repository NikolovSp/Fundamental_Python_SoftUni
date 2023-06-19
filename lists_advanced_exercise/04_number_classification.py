def number_clasification(some_numbers):
    positive_numbers = [n for n in some_numbers if n >= 0]
    negative_numbers = [n for n in some_numbers if n < 0]
    even_numbers = [n for n in some_numbers if n % 2 == 0]
    odd_numbers = [n for n in some_numbers if n % 2 != 0]
    # result = f'Positive: {positive_numbers}\nNegative:{negative_numbers}\nEven:{even_numbers}\nOdd:{odd_numbers}'
    # return result
    print('Positive: ', end='')
    print(*positive_numbers, sep=', ')
    print('Negative: ', end='')
    print(*negative_numbers, sep=', ')
    print('Even: ', end='')
    print(*even_numbers, sep=', ')
    print('Odd: ', end='')
    print(*odd_numbers, sep=', ')


numbers = [int(x) for x in input().split(',')]
number_clasification(numbers)
# print(result)
