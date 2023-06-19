chat_log = []
while True:
    chat_input = input().split()

    if chat_input[0] == 'end':
        break

    if chat_input[0] == 'Chat':
        chat_log.append(chat_input[1])

    if chat_input[0] == 'Delete':
        if chat_input[1] in chat_log:
            chat_log.remove(chat_input[1])
        else:
            continue

    if chat_input[0] == 'Edit':
        if chat_input[1] in chat_log:
            for i in range(len(chat_log)):
                if chat_log[i] == chat_input[1]:
                    chat_log[i] = chat_input[2]
        else:
            continue

    if chat_input[0] == 'Pin':
        if chat_input[1] in chat_log:
            for i in range(len(chat_log)):
                if chat_log[i] == chat_input[1]:
                    chat_log.pop(i)
                    chat_log.append(chat_input[1])
        else:
            continue

    if chat_input[0] == 'Spam':
        for i in range(1, len(chat_input)):
            chat_log.append(chat_input[i])


print(chat_log)
