def odd_and_even_sum(number):
    even_sum = 0
    odd_sum = 0

    while number > 0:
        last_digit = number % 10
        if last_digit % 2 == 0:
            even_sum += last_digit
        else:
            odd_sum += last_digit
        number = number // 10
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


num = int(input())
print(odd_and_even_sum(num))
