mounth=str(input())
spent_hours=int(input())
group=int(input())
time_of_day=str(input())
price_day=0
price_night=0
price=0
price_one=0
price_one_new=0

if mounth=='march' or mounth=='april' or mounth=='may':
    price_day=10.50
    price_night=8.40
    if group>=4 and time_of_day=='day':
        price_one = price_day*0.9
    elif group<4 and time_of_day=='day':
        price_one = price_day
    elif group>=4 and time_of_day=='night':
        price_one = price_night*0.9
    elif group<4 and time_of_day=='night':
        price_one=price_night

    if spent_hours >= 5 and time_of_day == 'day':
            price_one_new=price_day*0.5
            price = price_one-new * group * spent_hours
    elif spent_hours < 5 and time_of_day == 'day':
            price_one_new=price_day
            price= price_one_new * group * spent_hours
    elif spent_hours >= 5 and time_of_day == 'night':
            price_one_new=price_night*0.5
            price = price_one_new * group * spent_hours
    elif spent_hours < 5 and time_of_day == 'night':
            price_one_new=price_night
            price= price_one_new * group * spent_hours
if mounth=='june' or mounth=='july' or mounth=='august':
    price_day=12.60
    price_night=10.20
    if group>=4 and time_of_day=='day':
        price_one = price_day*0.9
    elif group<4 and time_of_day=='day':
        price_one = price_day
    elif group>=4 and time_of_day=='night':
        price_one = price_night*0.9
    elif group<4 and time_of_day=='night':
        price_one=price_night

    if spent_hours >= 5 and time_of_day == 'day':
            price_one_new=price_one*0.5
            price = price_one_new * group * spent_hours
    elif spent_hours < 5 and time_of_day == 'day':
            price_one=price_day
            price = price_one_new * group * spent_hours
    elif spent_hours >= 5 and time_of_day == 'night':
            price_one_new=price_one*0.5
            price = price_one_new * group * spent_hours
    elif spent_hours < 5 and time_of_day == 'night':
            price_one=price_night
            price= price_one_new * group * spent_hours
print(price_one_new)
print(price)







