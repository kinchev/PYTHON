input_array = [int(x) for x in input().split(", ")]
input_target_sum = int(input())


# def two_numbers_sum(array, target_sum):
#     for number in array:
#         numbers = {}
#         potential_target = target_sum - number
#         if potential_target in numbers:
#             return [potential_target, number]
#         else:
#             numbers[number] = True
#
#         return []
def two_numbers_sum(array, target_sum):
    array.sort()
    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer < right_pointer:
        current_sum = array[left_pointer] + array[right_pointer]
        if current_sum == target_sum:
            return [array[left_pointer], array[right_pointer]]
        elif current_sum < target_sum:
            left_pointer += 1
        elif current_sum > target_sum:
            right_pointer -= 1
    return []


print(two_numbers_sum(input_array, input_target_sum))
