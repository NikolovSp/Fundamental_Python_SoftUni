some_string = input().upper()
final_string = ''
repetitions = ''
current_symbol = ''

for index in range(len(some_string)):
    if not some_string[index].isdigit():
        current_symbol += some_string[index]
    else:  #have a number in the string.
        for next_symbol in range(index, len(some_string)):
            if not some_string[next_symbol].isdigit():
                break
            else:
                repetitions += some_string[next_symbol]
        final_string += current_symbol * int(repetitions)
        repetitions = ''
        current_symbol = ''
print(f'Unique symbols used: {len(set(final_string))}')
print(final_string)
