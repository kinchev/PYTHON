type_fuel = input().lower()
litres_inside = float(input())

if litres_inside >= 25:
    if type_fuel=='diesel':
        print(f'You have enough {type_fuel}.')
    elif type_fuel=='gas':
        print(f'You have enough {type_fuel}.')
    elif type_fuel=='gasoline':
        print(f'You have enough {type_fuel}.')
    else:
        print('Invalid fuel!')
elif litres_inside < 25:
    if type_fuel=="diesel":
        print(f'Fill your tank with {type_fuel:}!')
    elif type_fuel=='gas':
        print(f'Fill your tank with {type_fuel:}!')
    elif type_fuel=='gasoline':
        print(f'Fill your tank with {type_fuel:}!')
    else:
        print('Invalid fuel!')
