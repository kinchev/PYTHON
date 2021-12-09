from collections import deque

station = int(input())
queue = deque()
for _ in range(station):
    pump = [int(x) for x in input().split()]
    queue.append(pump)

for index in range(station):
    car_fuel = 0
    completed = True
    for petrol, distance in queue:

        car_fuel += petrol
        if distance > car_fuel:
            completed = False
            break
        car_fuel-=distance
    if completed:
        print(index)
        break
    else:
        queue.append(queue.popleft())
