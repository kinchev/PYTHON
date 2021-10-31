budget = int(input())
season = input()
fishers = int(input())
ship_price = 0

if season == "Spring":
    ship_price = 3000
elif season == "Summer" or season == "Autumn":
    ship_price = 4200
elif season == "Winter":
    ship_price = 2600

if fishers <= 6:
    ship_price = ship_price * 0.9
elif 7 <= fishers <= 11:
    ship_price = ship_price * 0.85
elif fishers > 11:
    ship_price = ship_price * 0.75

if fishers % 2 == 0 and season != "Autumn":
    ship_price == ship_price * 0.95

if budget >= ship_price:
    money_left = budget - ship_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = ship_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
