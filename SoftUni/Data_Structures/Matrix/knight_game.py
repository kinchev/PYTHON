n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))


def is_inside(board, row, col):
    board_size=len(board)
    if row < 0 or col < 0 or row >= board_size or col >= board_size:
        return False
    return board[row][col] == 'K'


def count_knights(board_size, row, col):
    result = 0

    if is_inside(board_size, row - 2, col - 1):
        result += 1
    if is_inside(board_size, row - 2, col + 1):
        result += 1
    if is_inside(board_size, row + 2, col - 1):
        result += 1
    if is_inside(board_size, row + 2, col + 1):
        result += 1
    if is_inside(board_size, row - 1, col - 2):
        result += 1
    if is_inside(board_size, row - 1, col + 2):
        result += 1
    if is_inside(board_size, row + 1, col + 2):
        result += 1
    if is_inside(board_size, row + 1, col - 2):
        result += 1
    return result


removed_knights = 0

while True:
    max_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == '0':
                continue
            count = count_knights(matrix, row, col)
            if count > max_count:
                max_count, knight_row, knight_col = count, row, col
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)
