companies_dict = {}

while True:
    current_command = input().split(' -> ')

    if current_command[0] == 'End':
        break

    current_company = current_command[0]
    current_ID = current_command[1]

    if current_company not in companies_dict.keys():
        companies_dict[current_company] = []

    if current_ID not in companies_dict[current_company]:
        companies_dict[current_company].append(current_ID)

for company in companies_dict.keys():
    print(f'{company}')
    for ID in companies_dict[company]:
        print(f'-- {ID}')
#Debugger doesn't work??? have to double check what's the error!
