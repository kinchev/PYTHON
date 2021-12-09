#
#
# cards = input().split()
# n_shuffles = int(input())
#
# top_card = cards[0]
# bottom_card = cards[-1]
#
# half = len(cards) // 2
# shuffle_card = []
# for n_shuffle in range(n_shuffles):
#     left_deck = []  # [cards[1:half]]
#     right_deck = []  # [cards[half:-1]]
#
#     # a b c d e f g h
#     # 5
#     for index in range(1, half):
#         left_deck.append(cards[index])
#     for index in range(half, len(cards) - 1):
#         right_deck.append(cards[index])
#
#     for index in range(len(left_deck)):
#         shuffle_card.append(right_deck[index])
#         shuffle_card.append(left_deck[index])
#     cards = shuffle_card.copy()
#     cards.append(bottom_card)
#     cards.insert(0, top_card)
#     shuffle_card = []
# print(cards)


# cards = input().split()
# n_faro = int(input())
# deck2_index = len(cards) // 2
# for _ in range(n_faro):
#     faro_cards = []
#     for index in range(deck2_index):
#         first_card = cards[index]
#         current2_index = index + deck2_index
#         second_card = cards[current2_index]
#         faro_cards.append(first_card)
#         faro_cards.append(second_card)
#     cards = faro_cards
#
# print(cards)

cards = input().split()
n_faro = int(input())
middle = len(cards) // 2
for _ in range(n_faro):
    current_shuffle = zip(
        cards[:middle], cards[middle:]
    )
    cards.clear()
    for pair in current_shuffle:
        cards.extend(pair)
print(cards)