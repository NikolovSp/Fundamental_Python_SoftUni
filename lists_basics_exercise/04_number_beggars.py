money = input().split(", ")
number_beggars = int(input())

list_money = [int(x) for x in money]
index = 0
final_money = []
while index < number_beggars:
    money_of_current_beggar = 0
    for current_index in range(index, len(list_money), number_beggars):
        money_of_current_beggar += list_money[current_index]
    final_money.append(money_of_current_beggar)
    index += 1
print(final_money)
