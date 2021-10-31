data = input().split()
product = {}
for i in range(len(data), 2):
    key = data[i]
    value = data[i + 1]
    product[key] = int(value)

search = input().split()
for s_product in search:
    if s_product not in product:
        print(f'Sorry, wwe don`t have{s_product}')
    else:
        print(f'We have {product[s_product]}')
