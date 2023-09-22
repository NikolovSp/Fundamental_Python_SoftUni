import re

pattern = r'^([$%])([A-Z][a-z]{2,})\1:\s*(\[\d+\]\|\[\d+\]\|\[\d+\]\|)$'
num_pattern = r'\[(\d+)\]'

n = int(input())

for i in range(n):
    message = input()

    match = re.match(pattern, message)
    if match:
        tag = match.group(2)
        numbers = re.findall(num_pattern, message)
        nums_as_ascii = []
        for num in numbers:
            nums_as_ascii.append(chr(int(num)))
        print(f'{tag}: {"".join(nums_as_ascii)}')
    else:
        print("Valid message not found!")
