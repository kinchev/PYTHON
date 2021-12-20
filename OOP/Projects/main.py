from ASTRONAUT.astronaut.biologist import Biologist
from ASTRONAUT.space_station import SpaceStation

print(Biologist.__name__)
space_station=SpaceStation()
print(space_station.add_astronaut('Biologist','P'))
print(space_station.add_astronaut('Biologist','P'))
print(space_station.retire_astronaut('P'))