def narcissistic(value):
    sum = 0
    power = len(str(value))
    value = str(value)
    for num in value:
        sum += int(num) ** power
    if sum == int(value):
        return True
    else:
        return False
