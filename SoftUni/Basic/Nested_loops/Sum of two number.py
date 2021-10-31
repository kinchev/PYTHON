start = int(input())
end = int(input())
target_num = int(input())
counter = 0
flag = False
for x in range(start, end + 1):
    for y in range(start, end + 1):
        combination = x + y
        counter += 1
        if combination == target_num:
            print(f'Combination N:{counter} ({x} + {y} = {target_num})')
            exit()



print(f'{counter} combinations - neither equals {target_num}')


