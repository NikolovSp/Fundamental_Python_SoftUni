def is_length_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False

def is_char_valid(username):
    if (username.isalnum() or '-' in username or '_' in username):
        return True
    return False

def no_space(username):
    if ' ' in username:
        return False
    return True


def is_password_valid(username):
    if is_length_valid(username) and is_char_valid(username) and no_space(username):
        return True
    return False

usernames = input().split(', ')
for username in usernames:
    if is_password_valid(username):
        print(username)
