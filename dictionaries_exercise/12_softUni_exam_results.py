results = {}
submissions = {}

while True:
    lines = input().split('-')

    if len(lines) == 1:
        break

    if len(lines) == 2:
        del results[lines[0]]
        continue
        #delete participant

    current_username, current_language, current_points = lines[0], lines[1], int(lines[2])

    if current_username not in results.keys():
        results[current_username] = 0
    if results[current_username] < current_points:
        results[current_username] = current_points

    if current_language not in submissions.keys():
        submissions[current_language] = 0
    submissions[current_language] += 1

print("Results:")
for username, points in results.items():
    print(f'{username} | {points}')
print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")
