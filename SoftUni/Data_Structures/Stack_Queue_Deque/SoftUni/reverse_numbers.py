from collections import deque

input_nums_as_str = input().split()
result = deque()
while input_nums_as_str:
    result.append(input_nums_as_str.pop())

print(" ".join(result))
