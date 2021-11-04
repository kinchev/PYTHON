name_air=input()
count_old=int(input())
count_kids=int(input())
neto_price_old=float(input())
price_service=float(input())

neto_price_kids=neto_price_old*0.3
bruto_price_old=neto_price_old+price_service
bruto_price_kids=40+neto_price_kids
total_price_all_tickets= (count_kids * bruto_price_kids) + (count_old * bruto_price_old)
profit=total_price_all_tickets*0.2
print(f'The profit of your agency from {name_air} tickets is {profit:.2f} lv.')

