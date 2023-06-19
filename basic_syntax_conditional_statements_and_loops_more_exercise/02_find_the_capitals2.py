letters = input()
capitals = list(filter(lambda x: letters[x].isupper(), range(len(letters))))
print(capitals)
