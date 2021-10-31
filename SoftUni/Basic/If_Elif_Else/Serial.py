budget = float(input())
# command -> име на актьор или ACTION
command = input()
# stop -> command == 'ACTION'
# continue -> command != 'ACTION'

while command != 'ACTION':
    # име на актьор
    actor_name = command
    salary = 0
    # > 15 -> заплата = 20% от бюджет
    # <= 15 -> заплата = вход
    if len(actor_name) > 15:
        salary = 0.2 * budget
    else:
        salary = float(input())

    budget -= salary
    if budget <= 0:
        break
    command = input()

# бюджетът е стигнал
if budget >= 0:
    print(f'We are left with {budget:.2f} leva.')
else:
    # -50 -> 50
    print(f'We need {abs(budget):.2f} leva for our actors.')v