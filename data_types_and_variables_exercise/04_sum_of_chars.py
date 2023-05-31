n = int(input())
sum_asci = 0
for i in range(n):
    char = input()
    sum_asci += ord(char)

print('The sum equals:', sum_asci)
