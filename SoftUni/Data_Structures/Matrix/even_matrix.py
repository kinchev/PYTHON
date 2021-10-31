row = int(input())
matrix = []
for n in range(row):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

evens = [[x for x in row if x % 2 == 0] for row in matrix]

print(evens)
