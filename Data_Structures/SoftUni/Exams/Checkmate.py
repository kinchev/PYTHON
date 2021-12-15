n = 8
matrix = []
for _ in range(n):
    matrix.append(input().split())


def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_right": (1, 1),
    "down_left": (1, -1),
}

queens = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "Q":
            for dir in direction:
                next_row = row + direction[dir][0]
                next_col = col + direction[dir][1]
                while is_in_range(next_row, next_col, n):
                    if matrix[row][col] == "Q":
                        break
                    if matrix[next_row][next_col] == "K":
                        queens.append(row, col)
                        break
                    next_row += direction[dir][0]
                    next_row += direction[dir][1]
