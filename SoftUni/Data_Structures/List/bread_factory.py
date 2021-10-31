tasks = input().split('|')
coins = 100
energy = 100
for task in tasks:
    events, value = task.split('-')
    value = int(value)
    if events == 'rest':
        if energy + value < 100:
            print(f"You gained {value} energy.")
            energy += value
            print(f'Current energy: {energy}.')
        elif energy + value >= 100:
            energy = 100
            print("You gained 0 energy.")
            print(f'Current energy: {energy}.')

    elif events == 'order':
        if energy >= 30:
            coins += value
            print(f"You earned {value} coins.")
            energy -= 30
        elif energy < 30:
            energy += 50
            print("You had to rest!")

    elif events != 'rest' and events != 'order':
        if coins <= value:
            print(f'Closed! Cannot afford {events}.')
            raise SystemExit  # quit() #exit()
        else:
            coins -= value
            print(f"You bought {events}.")
if coins > 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

# order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000
# day_events_list = input().split("|")
#
# MAX_ENERGY = 100
# ORDER_ENERGY = 30
# REST_ENERGY = 50
# energy = 100
# coins = 100
# is_not_bankrupt = True
#
# for event in day_events_list:
#     single_events_list = event.split("-")
#     name = single_events_list[0]
#     value = int(single_events_list[1])
#
#     if name == "rest":
#         gained_energy = 0
#
#         if energy + value > MAX_ENERGY:
#             gained_energy = MAX_ENERGY - energy
#             energy = MAX_ENERGY
#         else:
#             energy += value
#             gained_energy = value
#
#         print(f"You gained {gained_energy} energy.")
#         print(f"Current energy: {energy}.")
#
#     elif name == "order":
#         if energy >= ORDER_ENERGY:
#             energy -= ORDER_ENERGY
#             coins += value
#             print(f"You earned {value} coins.")
#         else:
#             energy += REST_ENERGY
#             print("You had to rest!")
#             continue
#
#     else:
#         if coins > value:
#             coins -= value
#             print(f"You bought {name}.")
#         else:
#             print(f"Closed! Cannot afford {name}.")
#             is_not_bankrupt = False
#             break
#
# #        if coins <= 0:
# #            is_not_bankrupt = False
# #            break
#
# if is_not_bankrupt:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {energy}")
