def ordering_names(given_names):
    ordered_names = sorted(given_names, key=lambda x: (-len(x), x))
    return ordered_names

names = input().split(', ')
result = ordering_names(names)
print(result)
