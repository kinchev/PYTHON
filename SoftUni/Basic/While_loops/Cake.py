width = int(input())
length = int(input())
cake_pieces = width * length
cake_is_over = False
command = input()
while command != 'STOP':
    current_pieces = int(command)
    cake_pieces += current_pieces
    if cake_pieces < 0:
        cake_is_over = True
        break
    command = input()
if cake_is_over:
    print('Mo more cake left!You need {abs(cake_pieces)}')
else:
    print(f'{cake_pieces} pieces left.')
