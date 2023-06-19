first_line = input().split()
second_line = input().split()
third_line = input().split()

print(first_line)
print(second_line)
print(third_line)

player_one_winner = False
player_two_winner = False
for i in range(2):
    if first_line[i] == second_line[i] == third_line[i] == '1':
        player_one_winner = True
        break
    # check rows if player one wins
    if first_line[i] == second_line[i] == third_line[i] == '2':
        player_two_winner = True
        break
for j in range(2):




if player_one_winner:
    print('First player won')
elif player_two_winner:
    print('Second player won')
else:
    print('Draw')

