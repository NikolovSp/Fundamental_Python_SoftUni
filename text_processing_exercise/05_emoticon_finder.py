sentence = [str(char) for char in input()]

for i in range(len(sentence)):
    if sentence[i] == ":":
        print(f"{sentence[i]}{sentence[i +1]}")
