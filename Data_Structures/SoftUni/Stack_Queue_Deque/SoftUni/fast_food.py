from collections import deque

quantity = int(input())
input_nums = [int(num) for num in input().split()]
print(max(input_nums))
queue = deque(input_nums)
while queue:
    if quantity - queue[0] < 0 or len(queue) == 0:
        print("Orders left: " + ' '.join([str(num) for num in queue]))
        break
    else:
        quantity -= queue.popleft()

if len(queue) == 0:
    print("Orders complete")
