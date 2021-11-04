n = int(input())
matrix = []

for _ in range(n):
    matrix.append([(x) for x in input()])

symbol = input()

for i in range(n):
    for j in range(n):
        if symbol == matrix[i][j]:
            print(f'({i}, {j})')
            raise exit()

print(f'{symbol} does not occur in the matrix')
