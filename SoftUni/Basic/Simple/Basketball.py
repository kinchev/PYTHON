year_tax = int(input())

basket_sneakers = year_tax - 0.4 * year_tax
basket_team = basket_sneakers - 0.2 * basket_sneakers
basket_ball = 0.25 * basket_team
basket_thing = 0.20 * basket_ball
sum = year_tax + basket_ball + basket_thing + basket_team + basket_sneakers
print(f'{sum:.2f}')
