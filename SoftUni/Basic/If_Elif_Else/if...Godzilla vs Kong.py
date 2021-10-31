budjet = float(input())
count_static = int(input())
price_clothes_per_one = float(input())
deckor = budjet * 0.1

if count_static > 150:
    money_clothes = price_clothes_per_one * count_static
    discount_clothes = money_clothes * 0.1
    money_clothes -= discount_clothes
else:
    count_static < 150
    money_clothes = price_clothes_per_one * count_static

total_money = deckor + money_clothes

if total_money > budjet:
    needed_money = total_money - budjet
    print('Not enough money!')
    print(f'Wingard needs {needed_money:.2f} leva more.')
elif total_money <= budjet:
    movie_money = deckor + money_clothes
    money_left = budjet - movie_money
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
