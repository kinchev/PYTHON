n = int(input())
school={}
count=1
for _ in range(0, n):
    name = input()
    grade = input()
    if name not in school:
        school[name]=float(grade)
    else:

        school[name]+=float(grade)
[print(f'{k} -> {v}')for k,v in school.items() if school[0][1]>4.50]
# 5
# Amanda
# 3.5
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6

