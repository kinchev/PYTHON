lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
volume_occupied_procent = float(input())
volume_of_aquarium = lenght_cm * width_cm * height_cm
total_liters = volume_of_aquarium * 0.001
volume_occupied_procent = volume_occupied_procent * 0.01
litres_needed = total_liters * (1 - volume_occupied_procent)
print(litres_needed)
