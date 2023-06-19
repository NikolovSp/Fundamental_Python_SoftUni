def factorial(a):
    result = 1
    for fact in range(a, 1, -1):
        result *= fact
    return result


def division(a, b):
    result = (factorial(a)) / (factorial(b))
    return f'{result:.2f}'

    # return f'{factorial(a) / factorial(b):/2f}'


num1 = int(input())
num2 = int(input())
print(division(num1, num2))
