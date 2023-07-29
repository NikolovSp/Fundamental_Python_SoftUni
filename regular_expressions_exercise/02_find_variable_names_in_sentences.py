import re

text = input()
pattern = r'\b_[A-Za-z0-9]+\b'
matches = re.findall(pattern, text)

final_match = []
for match in matches:
    match = match.replace('_', '')
    final_match.append(match)
print(','.join(final_match))
