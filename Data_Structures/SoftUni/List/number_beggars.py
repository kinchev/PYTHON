
# list1 = []
#
# for num in numbers:
#     if beggars == len(numbers):
#         print(numbers)
#         break
#     elif beggars > len(numbers):
#         zero = beggars - len(numbers)
#         count_zero = zero * [0]
#         a = numbers + count_zero
#         print(a)
#         break
#     else:
#         result_sum = [0] * beggars
#
#         for i in range(len(numbers)):
#             index = i % beggars
#             result_sum[index] += numbers[i]
# print(result_sum)

str_numbers = input().split(', ')
beggars = int(input())
numbers = list(map(int, str_numbers))
result = [0] * beggars
for i in range(len(numbers)):
    index = i % beggars
    result[index] += numbers[i]
print(result)
# 1, 2, 3, 4, 5
# 2
