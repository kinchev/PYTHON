(n, m) = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])
max_sum = 0
sums = []
for row in range(n - 1):
    for col in range(m - 1):
        current_sum = (
                matrix[row][col] +
                matrix[row + 1][col] +
                matrix[row + 1][col + 1] +
                matrix[row][col + 1]
        )
        if current_sum > max_sum:
            max_sum = current_sum
            position = (row, col)
row, col = position
print(matrix[row][col],matrix[row][col + 1])
print(matrix[row + 1][col],matrix[row + 1][col + 1])
print(max_sum)
