start_char = int(input())
end_char = int(input())

for asci in range(start_char, end_char + 1):
    print(chr(asci), end=" ")
