import re
pattern = r'([%$])([A-Z][a-z]+)\1: (\[\d+\]\|\[\d+\]\|\[\d+\])'

n = int(input())
for i in range(n):
    some_code = input()

    match = re.findall(pattern, some_code)
    if match:
        numbers = match[0][2].split('|')

    patterns_number = r'\[(\d+)\]'
    for num in numbers:
        list_num = re.findall(patterns_number, num)
        print(list_num, end=' ')