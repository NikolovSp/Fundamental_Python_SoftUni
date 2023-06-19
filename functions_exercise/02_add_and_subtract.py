def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


def add_and_subtract():
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    function_result = sum_numbers(num_1, num_2)
    print(subtract(function_result, num_3))

add_and_subtract()

