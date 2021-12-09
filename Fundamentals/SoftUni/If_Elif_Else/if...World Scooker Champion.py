etap = input()
kind_ticket = input()
count_ticket = int(input())
pictures = input()

price = 0
if etap == 'Final':
    if kind_ticket == 'Standard':
        price = 110.10
    elif kind_ticket == 'Premium':
        price = 160.66
    elif kind_ticket == 'VIP':
        price = 400
if etap == 'Semi final':
    if kind_ticket == 'Standard':
        price = 75.88
    elif kind_ticket == 'Premium':
        price = 125.22
    elif kind_ticket == 'VIP':
        price = 300.40
if etap == 'Quarter final':
    if kind_ticket == 'Standard':
        price = 55.50
    elif kind_ticket == 'Premium':
        price = 105.20
    elif kind_ticket == 'VIP':
        price = 118.90
total_ticket = price * count_ticket

if total_ticket > 4000 and pictures == "Y":
    final_ticket = total_ticket * 0.75
    print(f'{final_ticket:.2f}')
elif total_ticket > 4000 and pictures == 'N':
    final_ticket = total_ticket * 0.75
    print(f'{final_ticket:.2f}')
elif 2500 < total_ticket <= 4000 and pictures == 'Y':
    pictures = count_ticket * 40
    final_ticket = total_ticket * 0.9 + pictures
    print(f'{final_ticket:.2f}')
elif 2500 < total_ticket <= 4000 and pictures == 'N':
    final_ticket = total_ticket * 0.9
    print(f'{final_ticket:.2f}')
elif total_ticket < 2500 and pictures == 'N':
    final_ticket = total_ticket
    print(f'{final_ticket:.2f}')
elif total_ticket < 2500 and pictures == 'Y':
    pictures = count_ticket * 40
    final_ticket = total_ticket + pictures
    print(f'{final_ticket:.2f}')

