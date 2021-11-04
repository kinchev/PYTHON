# from collections import OrderedDict
#
# jane_facebook = {}
# command = input()
# while not command == "Log out":
#     command = command.split(': ')
#
#     what_do_to = command[0]
#
#     if what_do_to == 'New follower':
#         username = command[1]
#         if not username in jane_facebook:
#             likes = 0
#             comments = 0
#
#             jane_facebook[username] = likes, comments
#         else:
#             pass
#     elif what_do_to == 'Like':
#         username = command[1]
#         count = int(command[2])
#
#         if not username in jane_facebook:
#             jane_facebook[username][0] = count
#         else:
#             jane_facebook[username][0] += count
#     elif what_do_to == 'Comment':
#         username = command[1]
#         if not username in jane_facebook:
#             comments=1
#             jane_facebook[username] = comments
#
#
#         else:
#
#             jane_facebook[username][1] += 1
#     elif what_do_to == 'Blocked':
#         username = command[1]
#
#         if not username in jane_facebook:
#             print(f"{username} doesn't exist.")
#         else:
#             del jane_facebook[username]
#         # if username not in jane_facebook:
#
#     command = input()
#
# followers = len(jane_facebook.keys())
# print(f'{followers} followers')
# sum1 = 0
# sorted_pieces = dict(sorted(jane_facebook.items(), key=lambda x: (-x[1],x[0])))
#
# for key, values in sorted_pieces.items():
#     sum1 = sum(values.values())
#     print(f'{key}: {sum1}')
#
# # for key, value in sorted_jane_facebook:
# #     print(f'{key}: {total}')
# # Like: Katy: 3
# # Comment: Katy
# # New follower: Bob
# # Blocked: Bob
# # New follower: Amy
# # Like: Amy: 4
# # Log out
# #
# # Blocked: Amy
# # Comment: Amy
# # New follower: Amy
# # Like: Tom: 5
# # Like: Ellie: 5
# # Log out
#
# # New follower: George
# # Like: George: 5
# # New follower: George
# # Log out