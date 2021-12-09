count_people=int(input())
season=input()
total_price=0

if season =='spring':
    if count_people<=5:
        price=50.00
    elif count_people>5:
        price=48.00
    total_price=count_people*price
    print(f'{total_price:.2f} leva.')
elif season=='summer':
    if count_people<=5:
        price=48.50
    elif count_people>5:
        price=45.00
    total_price=count_people*price
    discount=total_price-(total_price*0.15)
    print(f'{discount:.2f} leva.')
elif season=='autumn':
    if count_people<=5:
        price=60.00
    elif count_people>5:
        price=49.50
    total_price=count_people*price
    print(f'{total_price:.2f} leva.')
elif season == 'winter':
    if count_people<=5:
        price=86.00
    elif count_people>5:
        price=85.00
    total_price = count_people * price
    up_price = total_price + (total_price * 0.08)
    print(f'{up_price:.2f} leva.')



