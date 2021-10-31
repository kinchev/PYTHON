import math

widht = float(input())
length = float(input())
height = float(input())
average_height_spaceman = float(input())

volume_spaceship = widht * length * height
volume_room = (average_height_spaceman + 0.40) * 2 * 2
space = volume_spaceship / volume_room

if 3 <= space <= 10:
    print(f'The spacecraft holds {math.floor(space)} astronauts.')
if space < 3:
    print(f'The spacecraft is too small.')
if space > 10:
    print(f'The spacecraft is too big.')
