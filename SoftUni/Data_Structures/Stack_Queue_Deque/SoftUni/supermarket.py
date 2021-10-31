# Tom is working at the supermarket, and he needs your help to keep track of his clients.
# Write a program which reads lines of input consisting of a customer's name and adds it to the end of a queue
# until "End" is received. If in a meantime you receive the command "Paid",
# you should print each customer in the order they are served (from the first to the last one) and empty the queue.
# When you receive "End", you should print the count of the remaining people in the queue in the format: "{count} people remaining."
from collections import deque

command = input()
clients = deque()
count = 0
while command != "End":
    if command == "Paid":
        for _ in range(len(clients)):
            print(clients.popleft())
            count-=1

    else:
        count+=1
        clients.append(command)

    command = input()
print(f"{count} people remaining.")