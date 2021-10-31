total_browers=int(input())
salary=int(input())
still_have_salary=True
for open_browers in range(total_browers):
    current_brower=input()
    if current_brower=='Facebook':
        salary-=150
    elif current_brower=='Instagram':
        salary-=100
    elif current_brower=='Reddit':
        salary-=50
    if salary<=0:
        still_have_salary=False
        break

if still_have_salary==True:
    print(salary)
else:
    print(f'You have lost your salary.')

