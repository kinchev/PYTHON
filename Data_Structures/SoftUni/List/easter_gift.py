# gifts = input().split()
# command = input().split()
#
# while True:
#     if command[0] == 'No' and command[1] == 'Money':
#         break
#
#     if command[0] == 'OutOfStock':
#         item = command[1]
#         for index, el in enumerate(gifts):
#             if el == item:
#                 gifts[index] = 'None'
#         # for index in range(len(gifts)):
#         #     if gifts[index] == item:
#         #         gifts[index] = 'None'
#     elif command[0] == 'Required':
#         item = command[1]
#         index = int(command[2])
#         if len(gifts) > index >= 0:
#             gifts[index] = item
#             # gifts = list(map(lambda word: word.replace(gifts[index], item), gifts))
#             # gifts = [gifts.replace(gifts[index], item)]
#         else:
#             pass
#     elif command[0] == 'JustInCase':
#         item = command[1]
#         gifts[-1] = item
#
#     command = input().split()
# for word in list(gifts):  # iterating on a copy since removing will mess things up
#     if word == 'None':
#         gifts.remove(word)
# print(' '.join(gifts))
# # Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes
# # OutOfStock Eggs
# # Required Spoon 2
# # JustInCase ChocolateEgg
# # No Money
# Sweets Cozonac Clothes Flowers Wine Clothes Eggs Clothes
# Required Paper 8
# OutOfStock Clothes
# Required Chocolate 2
# JustInCase Hat
# OutOfStock Cable
# No Money
gifts = input().split(' ')

command = input().split(' ')
while command[0] != 'No' and command[1] != 'Money':
    index = 0
    if command[0] == 'OutOfStock':
        gift = command[1]

        while gift in gifts:
            index = gifts.index(gift)
            gifts[index] = 'None'

    elif command[0] == 'Required':
        try:
            if len(gifts) > index >= 0:
                index = int(command[2])
                gifts[index] = command[1]

        except IndexError:
            pass

    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]

        command = input().split(' ')

while 'None' in gifts:
    gifts.remove('None')

for i in gifts:
    print(i, end=' ')
