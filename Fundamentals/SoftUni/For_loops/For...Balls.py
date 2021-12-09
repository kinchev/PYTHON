import math

n = int(input())
points =0
count=0
other=0
count_black=0
count_red=0
count_yellow=0
count_white=0
count_orange=0
for j in range(1, n + 1):
    balls = input()
    if balls == 'red':
        points += 5
        count_red+=1
    elif balls == 'orange':
        points += 10
        count_orange+=1
    elif balls == 'yellow':
        points += 15
        count_yellow += 1
    elif balls == 'white':
        points += 20
        count_white += 1
    elif balls == 'black':
        points /= 2
        count_black+=1
    else:
        other+=1
print(f'Total points: {math.floor(points)}')
print(f'Points from red balls: {count_red}')
print(f'Points from orange balls: {count_orange}')
print(f'Points from yellow balls: {count_yellow}')
print(f'Points from white balls: {count_white}')
print(f'Other colors picked: {other}')
print(f'Divides from black balls: {count_black}')
