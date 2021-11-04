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

# Primary
matrix = []
for i in range(n):
    [matrix[i][i] for i in range(n)]

# Secondary
[matrix[i][n - i - 1] for i in range(n)]
# below primary

below_diagonal = []
for row in range(n):
    for col in range(row):
        below_diagonal.append(matrix[row][col])

# Above primary diagonal
