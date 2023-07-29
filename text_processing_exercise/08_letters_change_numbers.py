some_string = input().split()

total_sum = 0

for each_string in some_string:
    current_sum = 0
    if each_string[0].islower():
        current_sum = int(each_string[1:-1]) * int(ord(each_string[0]) - 96)
        # print(current_sum)
    elif not each_string[0].islower():
        current_sum = int(each_string[1:-1]) / int(ord(each_string[0]) - 64)
        # print(current_sum)

    if each_string[-1].islower():
        current_sum += int(ord(each_string[-1]) - 96)
    elif not each_string[-1].islower():
        current_sum -= int(ord(each_string[-1]) - 64)

    total_sum += current_sum

print(f'{total_sum:.2f}')
