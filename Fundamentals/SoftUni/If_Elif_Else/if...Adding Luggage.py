price_luggage_up_20 = float(input())
kilo_luggage = float(input())
days_left = int(input())
count_luggage = int(input())

price_luggage_to_10 = price_luggage_up_20 * 0.2
price_luggage_from_10_to_20 = price_luggage_up_20 * 0.5

if days_left > 30:
    if kilo_luggage < 10:
        increase = price_luggage_to_10 + (price_luggage_to_10 * 0.10)
        total_price = count_luggage * increase
        print(f'The total price of bags is: {total_price:.2f} lv.')
    elif 10 < kilo_luggage < 20:
        increase = price_luggage_from_10_to_20 + (price_luggage_from_10_to_20 * 0.10)
        total_price = count_luggage * increase
        print(f'The total price of bags is: {total_price:.2f} lv.')
    elif kilo_luggage > 20:
        increase = price_luggage_up_20 + (price_luggage_up_20 * 0.10)
        total_price = count_luggage * increase
        print(f'The total price of bags is: {total_price:.2f} lv.')
elif 7 < days_left < 30:
    if kilo_luggage < 10:
        increase = price_luggage_to_10 + (price_luggage_to_10 * 0.15)
        total_price = count_luggage * increase
        print(f'The total price of bags is: {total_price:.2f} lv.')
    elif 10 < kilo_luggage < 20:
        increase = price_luggage_from_10_to_20 + (price_luggage_from_10_to_20 * 0.15)
        total_price = count_luggage * increase
        print(f'The total price of bags is: {total_price:.2f} lv.')
    elif kilo_luggage > 20:
        increase = price_luggage_up_20 + (price_luggage_up_20 * 0.15)
        total_price = count_luggage * increase
        print(f'The total price of bags is: {total_price:.2f} lv.')
elif days_left < 7:
    if kilo_luggage < 10:
        increase = price_luggage_to_10 + (price_luggage_to_10 * 0.40)
        total_price = count_luggage * increase
        print(f'The total price of bags is: {total_price:.2f} lv.')
    elif 10 < kilo_luggage < 20:
        increase = price_luggage_from_10_to_20 + (price_luggage_from_10_to_20 * 0.40)
        total_price = count_luggage * increase
        print(f'The total price of bags is: {total_price:.2f} lv.')
    elif kilo_luggage > 20:
        increase = price_luggage_up_20 + (price_luggage_up_20 * 0.40)
        total_price = count_luggage * increase
        print(f'The total price of bags is: {total_price:.2f} lv.')
