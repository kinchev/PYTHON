targeted_cities = {}

data = input()
while not data == "Sail":
    town, people, gold = data.split("||")
    people = int(people)
    gold = int(gold)

    if town not in targeted_cities:
        targeted_cities[town] = [0, 0]
    targeted_cities[town][0] += people
    targeted_cities[town][1] += gold
    data = input()

line = input()
while not line == "End":
    line = line.split("=>")
    command = line[0]
    town = line[1]
    if command == "Prosper":
        gold = int(line[2])
        if gold > 0:
            targeted_cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targeted_cities[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")
    elif command == "Plunder":
        people = int(line[2])
        gold = int(line[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        targeted_cities[town][0] -= people
        targeted_cities[town][1] -= gold
        if targeted_cities[town][0] <= 0 or targeted_cities[town][1] <= 0:
            targeted_cities.pop(town)
            print(f"{town} has been wiped off the map!")
    line = input()

targeted_cities = dict(sorted(targeted_cities.items(), key=lambda x: (-x[1][1], x)))
if len(targeted_cities) > 0:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for town in targeted_cities:
        print(f"{town} -> Population: {targeted_cities[town][0]} citizens, Gold: {targeted_cities[town][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")