n = int(input())
cars = {}
while n > 0:
    model, millage, fuel = input().split("|")
    millage = int(millage)
    fuel = int(fuel)
    cars[model] = {'millage': millage, 'fuel': fuel}

    n -= 1

command1 = input()

while True:

    command = command1.split(' : ')
    if command[0] == "Stop":
        break
    elif command[0] == 'Drive':
        model = command[1]
        millage = int(command[2])
        fuel = int(command[3])
        if cars[model]['fuel'] >= fuel:
            cars[model]['fuel'] -= fuel
            cars[model]['millage'] += millage
            print(f"{model} driven for {millage} kilometers. {fuel} liters of fuel consumed. ")
            if cars[model]['millage'] > 100000:
                cars[model].pop()
        else:
            print(f"Not enough fuel to make that ride")
            if cars[model]['millage'] > 100000:
                cars[model].pop()
    elif command[0] == 'Refuel':
        model = command[1]
        fuel = int(command[2])
        cars[model]['fuel'] += fuel
        if cars[model]['fuel'] > 75:
            cars[model]['fuel'] = 75
        print(f"{model} refueled with {fuel} liters")
    elif command[0] == 'Revert':
        model = command[1]
        millage = int(command[2])
        if cars[model]['millage'] - millage > 10000:
            print(f"{model} mileage decreased by {fuel} kilometers")

        elif cars[model]['millage'] - millage <= 10000:
            cars[model]['millage'] = 10000
            pass

    command1 = input()

for name,date in sorted(cars.items(),key=lambda x:-x[1][0],x[1])
# 3
# Audi A6|38000|62
# Mercedes CLS|11000|35
# Volkswagen Passat CC|45678|5
# Drive : Audi A6 : 543 : 47
# Drive : Mercedes CLS : 94 : 11
# Drive : Volkswagen Passat CC : 69 : 8
# Refuel : Audi A6 : 50
# Revert : Mercedes CLS : 500
# Revert : Audi A6 : 30000
# Stop
