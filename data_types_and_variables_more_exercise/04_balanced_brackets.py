number_lines = int(input())
brackets = []
Balanced = False
for count in range(number_lines):
    line = input()
    brackets.append(line)
print(brackets)
for index in range(number_lines - 1):
    if brackets[index] == ')':
        print('UNBALANCED')
        break
    elif brackets[index] == '(':
        for closing in range(index + 1, number_lines - 1):
            if brackets[closing] == ')':
                print('UNBALANCED')
                break
            elif brackets[closing] == ')':
                Balanced = True
if Balanced:
    print('BALANCED')
