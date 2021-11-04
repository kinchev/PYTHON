(n, m) = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

the_sum = 0

# 1.
# for row_index in range(n):
#     for column_index in range(m):
#         the_sum += matrix[row_index][column_index]

# 2.
# for row_index in range(n):
#     row = matrix[row_index]
#     the_sum += sum(row)
#
# print(the_sum)
print(sum(sum(row) for row in matrix))

print(matrix)



