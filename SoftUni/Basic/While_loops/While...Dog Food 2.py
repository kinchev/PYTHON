food_dog = int(input()) * 1000
command = input()
sum_eated_food = 0
food_dog_is_over = False
while command != 'Adopted':
    count_eat_food = int(command)
    sum_eated_food += count_eat_food
    if sum_eated_food <= food_dog:
        difference = food_dog - sum_eated_food
    break

    command = input()

if food_dog_is_over:
    print(f"Food is not enough. You need {abs(food_dog)} grams more.")

else:
    print(f"Food is enough! Leftovers: {food_dog} grams.")
