input_string = input()

meals_dict = {}
unliked_meals_counter = 0

while not input_string == "Stop":
    input_string_split = input_string.split("-")
    action = input_string_split[0]
    guest = input_string_split[1]
    meal = input_string_split[2]

    if action == "Like":
        if guest not in meals_dict:
            meals_dict[guest] = [meal]
        if meal not in meals_dict[guest]:
            meals_dict[guest].append(meal)

    elif action == "Unlike":
        if guest in meals_dict:
            if meal in meals_dict[guest]:
                unliked_meals_counter += 1

                meals_dict[guest] = [m for m in meals_dict[guest] if m != meal]

                print(f"{guest} doesn't like the {meal}.")

            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")

    input_string = input()

meals_dict = sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0]))

for key, value in meals_dict:
    print(f"{key}: {', '.join(value)}")

print(f"Unliked meals: {unliked_meals_counter}")