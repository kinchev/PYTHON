parentheses = input()
balanced = True
stack = []
for char in parentheses:
    if char in '{([':
        stack.append(char)
    else:
        if len(stack) == 0:
            balanced = False
            break
        last_opening_bracket = stack.pop()
        pair = f'{last_opening_bracket}{char}'
        if pair not in '(){}[]':
            balanced = False
            break

if balanced and len(stack) == 0:
    print('YES')
else:
    print('NO')
