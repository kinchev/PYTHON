n = int(input())
names_unique = set()
while n > 0:
    names_unique.add(input())
    n -= 1
for person in names_unique:
    print(person)