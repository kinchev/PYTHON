[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],

]
n = 5  # rows
m = 4  # columns

matrix_of_zeros = []

for _ in range(n):
    row = []
    for _ in range(m):
        row.append(0)

    matrix_of_zeros.append(row)

    print(row)

print()

for row in matrix_of_zeros:
    print(row)

print()

matrix_of_zeros = [[0] * m for _ in range(n)]
print(matrix_of_zeros)
