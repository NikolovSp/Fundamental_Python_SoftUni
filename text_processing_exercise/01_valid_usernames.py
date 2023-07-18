usernames_input = input().split(', ')

for username in usernames_input:
    if not 3 < len(username) < 16:
        continue
    if ' ' in username:
        continue
    if username.isalnum() or '-' in username or '_' in username:
        print(username)
