n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

primary_matrix = []
secondary_matrix = []
sum_primary = 0
sum_secondary = 0
for i in range(n):
    sum_primary += matrix[i][i]
    sum_secondary += matrix[i][n - 1 - i]

difference_of_matrix = sum_primary - sum_secondary
print(abs(difference_of_matrix))
