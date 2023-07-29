import re

sentence = input()
pattern = r'\s(([a-z0-9]+[a-z0-9\.\_\-]*)@([a-z\-]+)(\.[a-z]+)+)\b'
matched_mails = re.findall(pattern, sentence)
for extracted in matched_mails:
    print(extracted[0])
