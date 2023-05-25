number_of_strings = int(input())

for word in range(number_of_strings):
    string = input()

    for i in string:
        if i == ',' or i == '.' or i == '_':
            print(f'{string} is not pure!')
            break
    else:
        print(f'{string} is pure.')
