fire_ceil = input().split('#')
water_amount = int(input())

effort = 0
save_value = []
for fire in fire_ceil:
    data, value = fire.split(' = ')
    value = int(value)
    if water_amount < value:
        break
    elif data == 'High' and 81 <= value <= 125:
        water_amount -= value
        effort += value * 0.25
        save_value.append(value)

    elif data == 'Medium' and 51 <= value <= 80:
        water_amount -= value
        effort += value * 0.25
        save_value.append(value)

    elif data == 'Low' and 1 <= value <= 50:
        water_amount -= value
        effort += value * 0.25
        save_value.append(value)


print("Cells:")
for fire_value in save_value:
    print(f" - {fire_value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(save_value)}")

# High = 89#Low = 28#Medium = 77#Low = 23
# 1250
# High = 150#Low = 55#Medium = 86#Low = 40#High = 110#Medium = 77
# 220
