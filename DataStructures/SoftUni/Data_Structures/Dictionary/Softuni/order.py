products = {}
data = input()
while not data == 'buy':

    product, price, value = data.split()
    if product not in products:
        products[product] = float(price), int(value)
    else:
        products[product][1] += int(value)
        products[product][0] = float(price)
    data = input()
[print(f"{k} -> {v[0] * v[1]:.2f}") for k, v in products.items()]

# Beer 2.20 100
# IceTea 1.50 50
# NukaCola 3.30 80
# Water 1.00 500
# buy

# products = {}
# line = input()
#
# while not line == "buy":
#     product, price, value = line.split()
#     if product not in products:
#         products[product] = [float(price), int(value)]
#     else:
#         products[product][1] += int(value)
#         products[product][0] = float(price)
#     line = input()
#
# [print(f"{k} -> {v[0] * v[1]:.2f}") for k, v in products.items()]