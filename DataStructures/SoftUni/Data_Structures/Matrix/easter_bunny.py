n = int(input())
matrix = []
for row in range(n):
    elements = input().split()
    matrix.append(elements)
    for col in range(n):
        element = elements[col]
        if element == 'B':
            bunny_row, bunny_col = row, col


def is_inside(r, c, size):
    return 0 <= r < size or 0 <= c < size


directions = {
    'right': lambda r, c: (row, col + 1) 
    'left': lambda r, c: (row, col - 1),
    'up': lambda r, c: (row - 1, col),
    'down': lambda r, c: (row + 1, col)
}

max_eggs = 0
best_direction = ''
best_path = []

for direction, step in directions.items():
    eggs = 0
    current_row, current_col = bunny_row, bunny_col

    path = []

    while True:

        current_row, current_col = step(current_row, current_col)
        if not is_inside(current_row, current_col, n):
            break
        if matrix[current_row][current_col] == 'X':
            break
        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])
    if eggs > max_eggs:
        max_eggs, best_direction, best_path = eggs, direction, path

print(best_direction)
for step in best_path:
    print(step)
print(max_eggs)
