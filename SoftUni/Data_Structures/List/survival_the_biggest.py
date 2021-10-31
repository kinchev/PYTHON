numbers = list(map(int, input().split()))
n_remove = int(input())
for number in range(n_remove):
    numbers.remove(min(numbers))

print(', '.join(map(str, numbers)))





