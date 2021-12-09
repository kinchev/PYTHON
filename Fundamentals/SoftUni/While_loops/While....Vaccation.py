needed_money = float(input())
available_money = float(input())
spending_money = 0
total_days = 0
speding_too_much_days = False

while available_money < needed_money:
    action = input()
    current_sum = float(input())
    total_days += 1
    if action == 'save':
        available_money += current_sum
        spending_money = 0
    elif action == 'spend':
        available_money -= current_sum
        spending_money += 1
        if available_money < 0:
            available_money = 0
        if spending_money == 5:
            speding_too_much_days = True
            break
if speding_too_much_days:
    print('You can`t save money')
    print(total_days)

else:
    print(f'You save the money for {total_days}days.')
