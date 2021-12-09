n = int(input())
positive = []
negative = []

for num in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    if number < 0:
        negative.append(number)

print(positive)
print(negative)
print(f'Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}')
