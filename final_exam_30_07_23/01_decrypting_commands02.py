def make(text, case):
    if case == 'Upper':
        return text.upper()
    return text.lower()


def check(original_text,new_string):
    if new_string in original_text:
        return f'Message contains {new_string}'
    return f"Message doesn't contain {new_string}"


def replace(text, current_char, new_char):
    new_text = text.replace(current_char, new_char)
    return new_text


def cut(text, start_index, end_index):
    if 0 <= start_index <= len(text) and 0 <= end_index <= len(text):
        new_text = text[:start_index] + text[end_index + 1:]
        return new_text
    else:
        return None


def sum(text, start_index, end_index):
    if 0 <= start_index <= len(text) and 0 <= end_index <= len(text):
        sum_ascii = 0
        for char in range(start_index, end_index + 1):
            sum_ascii += ord(text[char])
        return sum_ascii
    return f'Invalid indices!'


some_string = input()

while True:
    command = input()
    if command == 'Finish':
        break
    command = command.split()
    if len(command) == 2:
        command, activity = command

        if command == 'Make':
            some_string = make(some_string, activity)
            print(some_string)

        if command == 'Check':
            print(check(some_string, activity))

    if len(command) == 3:
        command, activity, new_index = command

        if command == 'Replace':
            some_string = replace(some_string, activity, new_index)
            print(some_string)

        if command == 'Cut':
            cut_string = cut(some_string, int(activity), int(new_index))
            if cut_string is not None:
                some_string = cut_string
                print(some_string)
            else:
                print("Invalid indices!")

        if command == 'Sum':
            sum_ascii = sum(some_string, int(activity), int(new_index))
            print(sum_ascii)
