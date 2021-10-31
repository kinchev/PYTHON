clothes_stack = [int(num) for num in input().split()]
capacity = int(input())
count_rack = 1
sum_current_clothes = 0

while clothes_stack:
    if sum_current_clothes + clothes_stack[-1] > capacity:
        count_rack += 1
        sum_current_clothes = 0
    else:
        sum_current_clothes += clothes_stack.pop()

print(count_rack)
