n, m = [int(x) for x in input().split()]
matrix = []
for _ in range(n):
    matrix.append([(x) for x in input().split()])
is_equal = False
equal_sum = 0
for row in range(n - 1):
    for col in range(m - 1):
        if matrix[row][col] == matrix[row][col + 1] == \
                matrix[row + 1][col] == matrix[row][col + 1] == matrix[row + 1][col + 1]:
            equal_sum += 1
print(equal_sum)
