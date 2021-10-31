up_border_first=int(input())
up_border_second=int(input())
up_border_third=int(input())

for number1 in range(2,up_border_first+1,2):
    for number2 in range(2,up_border_second+1):
        for number3 in range(2,up_border_third+1,2):
            if number2==2 or number2==3 or number2==5 or number2==7:
                print(f'{number1} {number2} {number3}')

