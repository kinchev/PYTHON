items_to_buy = input().split('|')
budget = float(input())
bought_items = []

for item in items_to_buy:
    item, price = item.split('->')
    price = float(price)

    if budget < price:

        break
    elif item == 'Clothes' and price <= 50.00:
        budget -= price
        bought_items.append(price)
    elif item == 'Shoes' and price <= 35.00:
        budget -= price
        bought_items.append(price)
    elif item == 'Accessories' and price <= 20.50:
        budget -= price
        bought_items.append(price)
sum_items = sum(bought_items)
clients_prices = []

for prices in bought_items:
    new_price = prices * 1.40
    clients_prices.append(new_price)

sum_new = sum(clients_prices)
profit = sum_new - sum_items

for i in clients_prices:
    print(f'{i:.2f}', end=' ')

print()
print(f'Profit: {profit:.2f}')
total_sum = budget + sum_new

if total_sum >= 150.00:
    print('Hello, France!')
else:
    print("Time to go.")

# Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
# 120
# Shoes->41.20 | Clothes->20.30 | Accessories->40 | Shoes->15.60 | Shoes->33.30 | Clothes->48.60
# 90
