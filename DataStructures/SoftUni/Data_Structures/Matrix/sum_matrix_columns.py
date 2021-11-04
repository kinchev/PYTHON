(n, m) = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(" ")])

for i in range(m):

    column_sum = 0
    for j in range(n):
        column_sum += matrix[j][i]

    print(column_sum)
