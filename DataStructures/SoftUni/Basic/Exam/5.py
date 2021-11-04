target_day=float(input())
command=input()
price=0
earned_day=0
needed_money=0
while command!= 'closed' or earned_day>=target_day:

    if command== 'haircut':
        command2=input()
        if command2== 'mens':
            price=15

        if command2== 'ladies':
            price=20
        if command2== 'kids':
            price=10
        earned_day+=price

        command=input()

    elif command== 'color':
        command2=input()
        if command2== 'touch up':
            price=20
        if command2== 'full color':
            price=30
        earned_day+=price

        command = input()




if earned_day>=target_day:
    print(f'You have reached your target for the day')
else:
    needed_money=target_day-earned_day
    print(f'Target not reached! You need {needed_money:.0f}lv. more.')
print(f'Earned money: {earned_day}lv.')








