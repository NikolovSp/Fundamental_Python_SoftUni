n = int(input())
synonyms = {}

for i in range(n):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(F'{word} - {", ".join(synonyms[word])}')
