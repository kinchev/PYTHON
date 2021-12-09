input_length = [int(num) for num in input().split()]
set1 = set()
set2 = set()
for _ in range(input_length[0]):
    set1.add(int(input()))
for _ in range(input_length[1]):
    set2.add(int(input()))

intersection = set1.intersection(set2)
for repeat_el in intersection:
    print(repeat_el)

    # n, m = [int(num) for num in input().split()]
    # set1 = {input() for _ in range(n)}
    # set2 = {input() for _ in range(m)}
    # [print(num) for num in set1 & set2]
