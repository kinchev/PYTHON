n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])
primary_matrix = []
secondary_matrix=[]

for i in range(len(matrix)):
    secondary_matrix.append(matrix[i][n-1-i])
    primary_matrix.append(matrix[i][i])
print(f"Primary diagonal: {', '.join([str(x) for x in primary_matrix])}. Sum: {sum(primary_matrix)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_matrix])}. Sum: {sum(secondary_matrix)}")
