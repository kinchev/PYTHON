input_array = [int(x) for x in input().split(", ")]


def sorted_squared_array(array):
    new_array = [int(x * x) for x in array]

    new_array.sort()
    return new_array


print(sorted_squared_array(input_array))
