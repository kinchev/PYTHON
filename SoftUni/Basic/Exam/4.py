count_day=int(input())
total_degrees=0
degree_total_count=0
rakia_total_count=0
for day in range(count_day):
    count_rakia = float(input())
    degree_rakia=float(input())
    rakia_total_count+=count_rakia
    degree_total_count=count_rakia*degree_rakia
    total_degrees+=degree_total_count
print(f'Liter: {rakia_total_count:.2f}')
average_degrees= total_degrees / rakia_total_count
print(f'Degrees: {average_degrees:.2f}')
if average_degrees<38:
    print(f'Not good, you should baking!')
elif 38<average_degrees<42:
    print(f'Super!')
elif average_degrees>42:
    print(f'Dilution with distilled water!')

