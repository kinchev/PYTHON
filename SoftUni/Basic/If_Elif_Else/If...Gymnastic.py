country = input()
device = input()
hard = 0
performance = 0

if country == 'Russia':
    if device == 'ribbon':
        hard = 9.100
        performance = 9.400
    elif device == 'hoop':
        hard = 9.300
        performance = 9.800
    elif device == 'rope':
        hard = 9.600
        performance = 9.000
elif country == 'Bulgaria':
    if device == 'ribbon':
        hard = 9.600
        performance = 9.400
    elif device == 'hoop':
        hard = 9.550
        performance = 9.750
    elif device == 'rope':
        hard == 9.500
        performance == 9.400
elif country == 'Italy':
    if device == 'ribbon':
        hard = 9.200
        performance = 9.500
    elif device == 'hoop':
        hard = 9.450
        performance = 9.350
    elif device == 'rope':
        hard = 9.700
        performance = 9.150

total_rating = hard + performance
total_point = 20
left_point = total_point - total_rating
procent_to_max = (left_point / 20) * 100
print(f'The team of {country} get {total_rating:.3f} on {device}.')
print(f'{procent_to_max:.2f}%')
