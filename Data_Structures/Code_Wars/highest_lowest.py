def high_and_low(numbers):
    arr = []
    numbers = numbers.split(' ')
    numbers=[int(x)for x in numbers]
    max1 = max(numbers)
    arr.append(str(max1))

    min1 = min(numbers)
    arr.append(str(min1))
    return ' '.join(arr)