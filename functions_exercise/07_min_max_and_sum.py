numbers = input().split()

numbers = [int(x) for x in numbers]
print(f'The minimum number is {min(numbers)}')
print(f'The maximum number is {max(numbers)}')
print(f'The sum number is: {sum(numbers)}')
