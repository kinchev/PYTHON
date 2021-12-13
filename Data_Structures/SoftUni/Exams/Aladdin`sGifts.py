# from collections import deque
#
# materials = [int(x) for x in input().split()]
# magic_levels = [int(x) for x in input().split()]
# magic_levels = deque(magic_levels)
# dic = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}
#
#
# def check_sum(sum, material, magic):
#     if sum < 100:
#         sum = material * 2 + magic * 3
#         if 100 < sum < 200:
#             return "Gemstone"
#         elif 200 < sum < 300:
#             return "Porcelain Sculpture"
#         elif 300 < sum < 400:
#             return "Gold"
#         elif 400 < sum < 499:
#             return "Diamond Jewellery"
#
#
#
#     elif 200 > sum > 100:
#         return "Gemstone"
#     elif 200 < sum < 300:
#         return "Porcelain Sculpture"
#     elif 300 < sum < 400:
#         return "Gold"
#     elif 400 < sum < 499:
#         return "Diamond Jewellery"
#     else:
#         sum // 2
#         if 200 > sum > 100:
#             return "Gemstone"
#
#         elif 200 < sum < 300:
#             return "Porcelain Sculpture"
#         elif 300 < sum < 400:
#             return "Gold"
#         elif 400 < sum < 499:
#             return "Diamond Jewellery"
#
#
# list_present_gold = []
# list_present_gemstone = []
# while True:
#     if len(magic_levels) <= 0 or len(materials) <= 0:
#         break
#     else:
#         last_material = materials.pop()
#         first_level = magic_levels.popleft()
#
#         sum = last_material + first_level
#         present = check_sum(sum, last_material, first_level)
#         key = present
#         if key is None:
#             continue
#         else:
#             dic[key] += 1
#         if present == "Gemstone" or present == "Porcelain Sculpture":
#             if len(list_present_gemstone) == 0:
#                 list_present_gemstone.append(present)
#             else:
#                 if list_present_gemstone[len(list_present_gemstone) - 1] == present:
#                     print("The wedding presents are made!")
#                     list_present_gemstone.clear()
#         elif present == "Gold" or present == "Diamond Jewellery":
#             if len(list_present_gold) == 0:
#                 list_present_gold.append(present)
#             else:
#
#                 if list_present_gold[len(list_present_gold) - 1] == present:
#                     print("The wedding presents are made!")
#                     list_present_gemstone.clear()
#
# if magic_levels:
#     print("Magic left: " + ', '.join([str(x) for x in magic_levels]))
#
# if materials:
#     print("Magic left: " + ', '.join([str(x) for x in materials]))
#
# for key, value in dic.items():
#     if value == 0:
#         continue
#     else:
#         print(f"{key}: {value}")
