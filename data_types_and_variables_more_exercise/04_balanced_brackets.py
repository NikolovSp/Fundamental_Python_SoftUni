number_lines = int(input())
brackets = []
Balanced = True
for i in range(number_lines):
    random_string = input()

    if random_string == '(' or random_string == ')':
        brackets.append(random_string)

    if len(brackets) == 2:
        if brackets[0] == '(' and brackets[1] == ')':
            brackets.clear()
        else:
            Balanced = False

if len(brackets) != 0:
    Balanced = False

if Balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
