deck_of_cards = input().split()
faro_shuffles = int(input())

for shuffle in range(faro_shuffles):
    shuffled_deck = []
    middle_of_deck = len(deck_of_cards) // 2
    left_deck = deck_of_cards[:middle_of_deck]
    right_deck = deck_of_cards[middle_of_deck:]
    for index in range(middle_of_deck):
        shuffled_deck.append(left_deck[index])
        shuffled_deck.append(right_deck[index])
    deck_of_cards = shuffled_deck
print(shuffled_deck)
