def sign_of_multiplication(a, b, c):
    minus = 0
    list_nums = [a, b, c]
    for i in list_nums:
        if i < 0:
            minus += 1

        if i == 0:
            result = 'zero'
            return result

    if minus == 2 or minus == 0:
        result = 'positive'
    else:
        result = 'negative'

    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
result = sign_of_multiplication(num1, num2, num3)
print(result)
