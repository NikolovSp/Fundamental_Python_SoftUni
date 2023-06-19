def tribonacci_sequence(n):
    first = 0
    second = 0
    third = 0
    current = 1
    for _ in range(n):
        print(current, end=' ')

        first = second
        second = third
        third = current
        current = first + second + third

num = int(input())
tribonacci_sequence(num)
