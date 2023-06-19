def counter(beach_text):
    words_on_beach = ['sand', 'water', "fish", "sun"]
    counter = 0
    for ch in words_on_beach:
        while ch in beach_text:
            counter += 1
            beach_text = beach_text.replace(ch, "", 1)
    return counter


current_string = input().lower()
result = counter(current_string)
print(result)
