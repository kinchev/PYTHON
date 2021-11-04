
data = input()
products = {}
while not data == 'statistics':
    product, quantity = data.split(': ')
    quantity = int(quantity)
    if product not in products:
        products[product] = 0
    
    products[product] += quantity

    data = input()
print('Product in stock')
for product, quantity in products.items():
    print(f'-{product}:{quantity}')
print(f'Total Products: {len(product)}')
print(f'Total Quantity:{sum(products.values())}')
 