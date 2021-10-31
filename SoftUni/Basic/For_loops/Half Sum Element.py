import sys

count_numbers=int(input())
max_number=-sys.maxsize
sum_numbers=0
for number in range(count_numbers):
    current_number=int(input())
    if current_number>max_number:
        max_number=current_number
    sum_numbers+=current_number
if max_number==sum_numbers-max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    sum_others=sum_numbers-max_number
    print(f'Diff = {abs(max_number-sum_others)}')