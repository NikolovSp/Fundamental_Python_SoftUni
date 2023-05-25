event = input()
to_do_list = ['coding', 'dog', 'cat', 'movie']
TO_DO_LIST = ['CODING', 'DOG', 'CAT', 'MOVIE']
number_coffees_needed = 0

while event != 'END':

    if event not in to_do_list and event not in TO_DO_LIST:
        event = input()
        continue
    if event in to_do_list:
        number_coffees_needed += 1
    elif event in TO_DO_LIST:
        number_coffees_needed += 2

    event = input()

if number_coffees_needed > 5:
    print(f'You need extra sleep')
else:
    print(number_coffees_needed)
