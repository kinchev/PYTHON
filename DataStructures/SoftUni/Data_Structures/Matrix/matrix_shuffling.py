n, m = [int(x) for x in input().split()]
matrix = []
for _ in range(n):
    matrix.append([x for x in input().split()])


def is_valid_index(row, col, n1, m2):
    if row < 0 or col < 0 or row >= n1 or col >= m2:
        return False
    return True


while True:
    command = input().split()
    if command[0] == "END":
        break
    if command[0] != "swap" or len(command) != 5:
        print('Invalid input!')
        continue
    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if not is_valid_index(row1, col1, n, m) or not is_valid_index(row2, col2, n, m):
        print('Invalid input!')
        continue

    if command[0] == 'swap':
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for element in matrix:
            print(" ".join([str(x) for x in element]))
