type_fuel = input()
quantity = float(input())
club_card = input()

if type_fuel == 'Gasoline' and club_card=='Yes':
    price = 2.22
    total_price_1l = price - 0.18
elif type_fuel=='Gasoline' and club_card == 'No':
    price = 2.22
    total_price_1l = price

if type_fuel == 'Diesel'and  club_card == 'Yes':
    price = 2.33
    total_price_1l = price - 0.12
elif type_fuel=='Diesel' and club_card == 'No':
    price = 2.33
    total_price_1l = price
if type_fuel == 'Gas'and club_card == 'Yes':
    price = 0.93
    total_price_1l = price - 0.08
elif type_fuel=='Gas' and club_card == 'No':
    price = 0.93
    total_price_1l = price
total_price = quantity * total_price_1l

if 20 < quantity <= 25:
    final_price = total_price * 0.92
    print(f'{final_price:.2f} lv.')
elif quantity > 25:
    final_price = total_price * 0.9
    print(f'{final_price:.2f} lv.')
elif quantity<20:
    final_price=total_price
    print(f'{final_price:.2f} lv.')