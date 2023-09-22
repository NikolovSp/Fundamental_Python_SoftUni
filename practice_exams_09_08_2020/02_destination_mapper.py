import re
locations = []
sum = 0
pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'

given_locations = input()

matched_locations = re.findall(pattern, given_locations)

for i in range(len(matched_locations)):
    locations.append(matched_locations[i][1])
    sum += len(matched_locations[i][1])

print(f'Destinations: {", ".join(locations)}')
print(f"Travel Points: {sum}")
