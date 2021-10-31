number = int(input())
for current_number in range(1111, 10000):
    special_number = True
    for digit in (str(current_number)):
        current_digit = int(digit)
        if current_digit == 0 or number % current_digit != 0:
            special_number = False
            break
    if special_number:
        print(current_number, end=' ')
