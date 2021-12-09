numbers = input().split(' ')
int_numbers = list(map(int, numbers))
opposite_number = [-i for i in int_numbers]
print(opposite_number)
