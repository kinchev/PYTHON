food_dog = int(input()) * 1000
comand = input()
sum = 0
need_food = 0
left_food = 0
while comand != 'Adopted':
    count_eat_food = int(comand)
    sum += count_eat_food
    comand = input()
    if comand == 'Adopted':
        break

if sum <= food_dog:
    left_food = food_dog - sum
    print(f"Food is enough! Leftovers: {left_food} grams.")
else:
    need_food = sum - food_dog
    print(f"Food is not enough. You need {need_food} grams more.")
