record_seconds = float(input())
distance_metres = float(input())
time_seconds_for_1m = float(input())
delay = distance_metres // 15 * 12.5
new_time = distance_metres * time_seconds_for_1m + delay
if new_time<record_seconds:
    print(f'Yes, he succeeded! The new world record is {new_time:.2f} seconds.')
else:
    diffrence=new_time-record_seconds
    print(f'No, he failed! He was {diffrence:.2f} seconds slower.')