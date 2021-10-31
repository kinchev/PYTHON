day_of_stay = int(input())
type_of_room = input()
rating = input()

nights = day_of_stay - 1
price_per_night = 0

if type_of_room == 'room for one person':
    price_per_night = 18
elif type_of_room == 'apartment':
    price_per_night = 25
elif type_of_room == 'president apartment':
    price_per_night = 35

total_price = nights * price_per_night

if type_of_room == 'apartment':
    if day_of_stay < 10:
        total_price = 0.7 * total_price
    elif 10 <= day_of_stay <= 15:
        total_price = 0.65 * total_price
    elif day_of_stay > 15:
        total_price = 0.5 * total_price

elif type_of_room == 'president apartment':
    if day_of_stay < 10:
        total_price = 0.9 * total_price
    elif 10 <= day_of_stay <= 15:
        total_price = 0.85 * total_price
    elif day_of_stay > 15:
        total_price = 0.8 * total_price

if rating == 'positive':
    total_price = total_price * 1.25
elif rating == 'negative':
    total_price = total_price * 0.9

print(f'{total_price:.2f}')
