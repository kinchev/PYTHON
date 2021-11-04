pocket_money=float(input())
day_profit=float(input())
all_costs=float(input())
price_gift=float(input())
save_pocket_money=5*pocket_money
earn_money=5*day_profit
total_save_money=save_pocket_money+earn_money
money_after_costs=total_save_money-all_costs
need_money=0
if money_after_costs>price_gift:
    print(f'Profit: {money_after_costs:.2f} BGN, the gift has been purchased.')
else:
    money_after_costs<price_gift
    need_money=price_gift-money_after_costs
    print(f'Insufficient money: {need_money:.2f} BGN.')