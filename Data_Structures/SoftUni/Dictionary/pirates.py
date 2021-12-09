town_input = input()
dict_town = {}
while not town_input == 'Sail':
    town, people, gold = town_input.split("||")
    dict_town[town] = [int(people), int(gold)]

    town_input = input()

command = input()

while not command == 'End':
    command = command.split('=>')
    what = command[0]
    if what == 'Plunder':
        town = command[1]
        people = command[2]
        gold = command[3]
        dict_town[town][0] -= int(people)
        dict_town[town][1] -= int(gold)
        if dict_town[town][0] <= 0 or dict_town[town][1] <= 0:
            del dict_town[town]
            print(f"{town} has been wiped off the map!")
        else:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    elif what == 'Prosper':
        town = command[1]
        gold = int(command[2])
        if gold > 0:
            dict_town[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dict_town[town][1]} gold.")

        else:
            print(f"Gold added cannot be a negative number!")

    command = input()

# Tortuga||345000||1250
# Santo Domingo||240000||630
# Havana||410000||1100
# Sail
# Plunder=>Tortuga=>75000=>380
# Prosper=>Santo Domingo=>180
# End
# Tortuga||345000||1250
# Santo Domingo||240000||630
# Havana||410000||1100
# Sail
# Plunder=>Tortuga=>75000=>380
# Prosper=>Santo Domingo=>-180
# End
city_target=dict(sorted(dict_town.items(), key=lambda x: (-x[1][1], x)))

if len(dict_town)<0:
    print('"Ahoy, Captain! All targets have been plundered and destroyed!" ')
else:
    print(f'Ahoy, Captain! There are {len(dict_town)} wealthy settlements to go to:')
    for town in city_target:

        print(f"{town} -> Population: {city_target[town][0]} citizens, Gold: {city_target[town][1]} kg")
