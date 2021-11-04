import sys

n, m = [int(x) for x in input().split()]
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
max_sum = -sys.maxsize
best_row = None
best_col = None
for row in range(n - 2):
    for col in range(m - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                      matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                      matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if current_sum > max_sum:
            max_sum, best_row, best_col = current_sum, row, col

print(f'Sum = {max_sum}')
print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col + 2])
print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col + 2])
print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col + 2])
