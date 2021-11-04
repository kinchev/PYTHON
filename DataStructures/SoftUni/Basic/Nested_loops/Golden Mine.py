places_gold = int(input())
count_day_gold = 0
average_dig_gold = 0
need=0
for lacaton in range(1,places_gold+1):
    expected_gold = int(input())
    day_digging_gold = int(input())
    for day in range(1,day_digging_gold+1):
        day_gold = int(input())
        count_day_gold += day_gold
        average_dig_gold = count_day_gold / day_digging_gold

    if average_dig_gold>=expected_gold:
        print(f'God job! Average gold per day:{average_dig_gold:.2f}.')
        count_day_gold=0
        average_dig_gold=0
    elif average_dig_gold<expected_gold:
        need=expected_gold-average_dig_gold
        print(f'You need {need:.2f} gold')
        count_day_gold=0
        average_dig_gold=0









































