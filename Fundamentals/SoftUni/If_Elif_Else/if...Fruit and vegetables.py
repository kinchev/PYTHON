
fruit_vegetables_unknown=input()

if fruit_vegetables_unknown=='banana' or fruit_vegetables_unknown=='apple' or fruit_vegetables_unknown=='kiwi' \
        or fruit_vegetables_unknown=='cherry'\
        or fruit_vegetables_unknown=='lemon' or fruit_vegetables_unknown=='grapes':
    print('fruit')
elif  fruit_vegetables_unknown=='tomato' or fruit_vegetables_unknown=='cucumber' or fruit_vegetables_unknown=='pepper'\
        or fruit_vegetables_unknown=='carrot':
    print('vegetable')
else:
    print('unknown')