flours = int(input())
apartamnet = int(input())

for f in range(flours, 0, -1):
    for a in range(0,apartamnet):
        if f==flours:
            print(f'L{f}{a}', end=' ')
        elif f%2==0:
            print(f'O{f}{a}', end=' ')
        else:
            print(f'A{f}{a}', end=' ')
    print()

