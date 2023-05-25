first_string = input()
second_string = input()

last_string = first_string

for i in range(len(first_string)):
    right_side = first_string[i + 1:]
    left_side = second_string[:i + 1]
    final_string = left_side + right_side

    if final_string == last_string:
        continue

    print(final_string)
    last_string = final_string
