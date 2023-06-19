times = list(map(int, input().split()))
left_driver_time = 0
right_driver_time = 0

for index_left in range(len(times)//2):
    if times[index_left] == 0:
        left_driver_time *= 0.80
    left_driver_time += times[index_left]

for right_index in range(len(times) - 1, len(times)//2, -1):
    if times[right_index] == 0:
        right_driver_time *= 0.80
    right_driver_time += times[right_index]

if left_driver_time < right_driver_time:
    print(f"The winner is left with total time: {left_driver_time:.1f}")
else:
    print(f"The winner is right with total time: {right_driver_time:.1f}")
