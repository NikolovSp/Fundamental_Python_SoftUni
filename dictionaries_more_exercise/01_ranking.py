contests_dict = {}
participants_dict = {}
contests = input()

while contests != 'end of contests':

    contest, password = contests.split(':')
    contests_dict[contest] = password

    contests = input()
# print(contests_dict)

submissions = input()

while submissions != "end of submissions":
    contest, password, username, points = submissions.split('=>')
    if contest in contests_dict and password in contests_dict[contest]:
        if username not in participants_dict.keys():
            participants_dict[username] = []
        participants_dict[username].append({contest, points})

    submissions = input()

print(participants_dict)
