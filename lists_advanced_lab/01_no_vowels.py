def volwes_remove(some_word):
    volwes = ['a', 'o', 'u', 'e', 'i']
    new_word = [char for char in some_word if char.lower() not in volwes]

    return ''.join(new_word)

word = input()
print(volwes_remove(word))
