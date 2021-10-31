n = int(input())
sum_even = 0
sum_odd = 0
for numbers in range(0, n):
    number = int(input())
    if numbers % 2:
        sum_even+=number
    else:
        sum_odd+=number

if sum_odd==sum_even:
    print('Yes')
    print(f'Sum = {sum_odd}')
else:
    difference=sum_even-sum_odd
    print('No')
    print(f'Diff = {abs(difference)} ')
