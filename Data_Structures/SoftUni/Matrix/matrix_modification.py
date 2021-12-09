n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])


def is_valid(row_index, col_index, size):
    if 0 <= row_index < size and 0 <= col_index < size:
        return True
    return False


command = input().split()

while command[0] != "END":
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if command[0] == "Add":

        if is_valid(row, col, n):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    elif command[0] == "Subtract":

        if is_valid(row, col, n):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    command = input().split()

for elements in matrix:
    print(' '.join([str(x) for x in elements]))
