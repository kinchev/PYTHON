roll_paper=int(input())
roll_cloth=int(input())
litres_glue=float(input())
pro_discount=int(input())
paper=5.80
cloth=7.20
glue=1.20
price_roll=roll_paper*paper
price_cloth=roll_cloth*cloth
price_glue=litres_glue*glue
all_materials=price_glue+price_roll+price_cloth
discount_price=all_materials-(all_materials*pro_discount/100)
print(f'{discount_price:.3f}')
a=int(input())
b=int(input())