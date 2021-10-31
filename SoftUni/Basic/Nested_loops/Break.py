start=int(input())
end=int(input())
magic_num=int(input())
counter=0
flag=False
for x in range(start,end+1):
    for y in range(start,end+1):
        sum=x+y
        counter+=1
        if sum==magic_num:
            print(f'Combination N:{counter} {x} + {y} = {sum}')
            flag=True
            break
    if flag:
        break
if flag !=True:
    print(f'{counter} combination - neither equal {sum}')