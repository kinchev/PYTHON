import sys

count_numbers = int(input())
sum_odd = 0
max_odd = -sys.maxsize
min_odd = sys.maxsize
sum_even = 0
max_even = -sys.maxsize
min_even = sys.maxsize
for position in range(1, count_numbers + 1):
    current_number=float(input())
    if position%2==0:
        sum_even+=current_number
        if current_number>max_even:
            max_even=current_number
        if current_number<min_even:
            min_even=current_number
    else:
        sum_odd += current_number
        if current_number > max_odd:
            max_odd = current_number
        if current_number < min_odd:
            min_odd = current_number
print(f'OddSum={sum_odd:.2f},')
if min_odd==sys.maxsize:
    print(f'OddMin=No,')
else:
    print(f'OddMin={min_odd:.2f},')
if max_odd==-sys.maxsize:
    print(f'OddMax=No,')
else:
    print(f'OddMax={max_odd:.2f},')
print(f'EvenSum={sum_even:.2f},')
if min_even==sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={min_even:.2f},')
if max_even==-sys.maxsize:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={max_even:.2f}')





