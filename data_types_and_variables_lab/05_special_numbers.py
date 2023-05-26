n = int(input())

for num in range(1, n + 1):
    sum = 0
    a = num

    while a > 0:
        sum += num % 10
        a = int(a / 10)
    if sum % 5 == 0 or sum % 7 == 0 or sum % 11 == 0:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
