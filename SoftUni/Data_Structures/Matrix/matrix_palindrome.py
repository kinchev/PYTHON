n, m = [int(x) for x in input().split()]

for row in range(n):
    for col in range(m):
        print(f'{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}', end=" ")
    print()
