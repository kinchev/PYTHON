days = int(input())
hours_per_day = int(input())

price = 0
price_per_day = 0

for day in range(1, days + 1):
    if day > 1:
        print(f'Day: {day - 1} - {price_per_day:.2f} leva')
    price += price_per_day
    price_per_day = 0
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and not hour % 2 == 0:
            price_per_day += 2.50
        elif not day % 2 == 0 and hour % 2 == 0:
            price_per_day += 1.25
        else:
            price_per_day += 1

price += price_per_day
print(f'Day: {day} - {price_per_day:.2f} leva')
print(f'Total: {price:.2f} leva')





count_day=int(input())
count_hours_for_day=int(input())
price=0
final_price=0
for day in range(1,count_day+1):
    count_price_for_day = 0
    for hours in range(1,count_hours_for_day+1):
        if day % 2==0 and hours % 2==1:
            price=2.50
        elif day % 2==1 and hours % 2==0:
            price=1.25
        else:
            price=1
        count_price_for_day+=price
    print(f'Day: {day} - {count_price_for_day:.2f} leva')
    final_price += count_price_for_day
print(f'Total: {final_price:.2f} leva')












