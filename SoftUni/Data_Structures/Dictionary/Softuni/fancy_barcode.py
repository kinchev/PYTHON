import re

pattern = r'(@#+)[A-Z][A-Za-z0-9]{4,}[A-Z](\1)'
n = int(input())
for _ in range(n):
    code = input()
    if re.match(pattern, code):
        digits = re.findall(r"\d", code)
        if digits:
            print(f"Product group: {''.join(digits)}")

        else:
            print(f'Product group: 00')
    else:
        print('Invalid barcode')
