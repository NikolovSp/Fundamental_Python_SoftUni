def take_odd(word):
    new_password = ''
    for i in range(1, len(word), 2):
        new_password += word[i]
    return new_password


def cut(word, index, length):
    new_password = word[:index] + word[index + length:]
    return new_password


def substitute(word, old_string, replacement):
    if old_string in word:
        return word.replace(old_string, replacement)
    else:
        return None



password = input()
new_word = ''
command = input()

while command != 'Done':

    if ' ' not in command:
        password = take_odd(password)
        print(password)
    else:
        command = command.split(' ')

        if command[0] == 'Cut':
            password = cut(password, int(command[1]), int(command[2]))
            print(password)
        elif command[0] == 'Substitute':
            message = substitute(password, command[1], command[2])
            if message is not None:
                password = message
                print(password)
            else:
                print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")
