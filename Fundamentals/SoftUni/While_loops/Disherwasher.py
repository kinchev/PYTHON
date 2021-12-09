number_of_bottles = int(input())
amount_of_detergent = number_of_bottles * 750
No_more_detergent = False
command = input()
current_number = 0
cost = 0
sum_cost = 0
sum_pots = 0
sum_plates = 0
while command != "End":
    current_amount_of_dishes = int(command)
    current_number += 1
    if current_number % 3 == 0:
        cost = current_amount_of_dishes * 15
        sum_cost += cost
        sum_pots += current_amount_of_dishes
    else:
        cost = current_amount_of_dishes * 5
        sum_cost += cost
        sum_plates += current_amount_of_dishes
    if sum_cost > amount_of_detergent:
        No_more_detergent = True
        break
    command = input()
if No_more_detergent:
    needed_detergent = sum_cost - amount_of_detergent
    print(f"Not enough detergent, {needed_detergent} ml. more necessary!")
else:
    left_detergent = amount_of_detergent - sum_cost
    print("Detergent was enough!")
    print(f"{sum_plates} dishes and {sum_pots} pots were washed.")
    print(f"Leftover detergent {left_detergent} ml.")
