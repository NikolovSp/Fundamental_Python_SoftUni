import re

dates = input()
regex = r'(\d{2})([/.-])([A-Z][a-z]{2})\2(\d{4})'
matches = re.findall(regex, dates)

# print(matches)
for match in matches:
    date = match[0]
    month = match[2]
    year = match[3]
    print(f'Day: {date}, Month: {month}, Year: {year}')
