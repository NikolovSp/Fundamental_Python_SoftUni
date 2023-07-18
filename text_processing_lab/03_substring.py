to_remove_string = input()
text = input()
while to_remove_string in text:
    text = text.replace(to_remove_string, '')

print(text)
