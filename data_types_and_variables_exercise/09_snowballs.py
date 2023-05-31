from sys import maxsize

snowballs_made = int(input())
best_snowball = -maxsize

for snowball in range(snowballs_made):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    snowball_value = (weight / time_needed) ** quality

    if snowball_value > best_snowball:
        best_snowball = snowball_value
        top_weight = weight
        top_time = time_needed
        top_quality = quality

print(f'{top_weight} : {top_time} = {best_snowball:.0f} ({top_quality})')
