n = int(input())
total_volume = 255

for pouring in range(n):
    flow = int(input())

    if total_volume - flow < 0:
        print('Insufficient capacity!')
        continue
    total_volume -= flow

print(255 - total_volume)
