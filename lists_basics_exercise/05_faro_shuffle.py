list_cards = input().split()
faro_shuffles = int(input())

for shuffles in range(faro_shuffles):
    shuffled_list = []
    for index in range(0, (len(list_cards) // 2)):
        shuffled_list.append(list_cards[index])
        shuffled_list.append(list_cards[index + (len(list_cards) // 2)])
    list_cards = shuffled_list

print(shuffled_list)

# for one shuffle only
# left_side = []
# right_side = []
#
# for left_side_index in range(0, (len(list_cards) // 2)):
#     left_side.append(list_cards[left_side_index])
#
# for right_side_index in range((len(list_cards) // 2), len(list_cards)):
#     right_side.append(list_cards[right_side_index])
#
# print(left_side)
# print(right_side)
# print(shuffled_list)
