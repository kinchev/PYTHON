price_one_pege=float(input())
price_one_cover=float(input())
procent_discount_paper=int(input())
sum_designers=float(input())
procent_from_total_price=float(input())

start_sum=price_one_pege*899+price_one_cover*2
after_discount=start_sum-(start_sum*procent_discount_paper/100)
sum_with_designers=after_discount+sum_designers
team_sum=sum_with_designers-(sum_with_designers*procent_from_total_price/100)
print(f'Avtonom should pay {team_sum:.2f} BGN.')