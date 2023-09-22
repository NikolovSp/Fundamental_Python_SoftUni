followers = {}

while True:
    command = input()
    if command == "Log out":
        break

    command = command.split(': ')
    if len(command) == 2:
        username = command[1]

        if command[0] == "New follower":
            if username not in followers:
                followers[username] = {'likes': 0, 'comments': 0}

        if command[0] == "Comment":
            if username not in followers:
                followers[username] = {'likes': 0, 'comments': 0}
            followers[username]['comments'] += 1

        if command[0] == "Blocked":
            if username in followers:
                del followers[username]
            else:
                print(f"{username} doesn't exist.")

    if len(command) == 3:
        username = command[1]
        like = int(command[2])
        if command[0] == "Like":
            if username not in followers:
                followers[username] = {'likes': 0, 'comments': 0}
            followers[username]['likes'] += like

print(f'{len(followers.keys())} followers')
# print(followers)

for key, value in followers.items():
    # sum = int(followers[key]['likes']) + int(followers[key]['comments'])
    print(f"{key}: {int(followers[key]['likes']) + int(followers[key]['comments'])}")
