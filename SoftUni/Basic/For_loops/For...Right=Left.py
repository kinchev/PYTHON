n = int(input())
left_sum = 0
right_sum = 0
for numbers in range(2 * n):
    number = int(input())
    if numbers < n:
        left_sum += number
    else:
        right_sum += number
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    differnce = abs(left_sum - right_sum)
    print(f'No, diff = {differnce}')
