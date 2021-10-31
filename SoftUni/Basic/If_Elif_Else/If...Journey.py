budjet=float(input())
season=input()
spent_money=0
destination=''
place=''
if budjet<=100:
    destination='Bulgaria'
    if season=='summer':
        spent_money=budjet*0.3
        place='Camp'
    else:
        season=='winter'
        spent_money=budjet*0.7
        place='Hotel'
elif budjet<=1000:
    destination='Balkans'
    if season=='summer':
        spent_money=budjet*0.4
        place='Camp'
    else:
        season=='winter'
        spent_money=budjet*0.8
        place='Hotel'
elif budjet>1000:
    destination = 'Europe'
    if season == 'summer':
        spent_money = budjet * 0.9
        place = 'Hotel'
    else:
        season == 'winter'
        spent_money=budjet*0.9
        place='Hotel'

print(f'Somewhere in {destination}')
print(f'{place} - {spent_money:.2f}')