import counter as counter

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()
        self.failed_mission = 0
        self.successful_mission = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added"
        astronaut = self.__create_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}"

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added'
        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added {planet}"

    def retire_astronaut(self, name: str):
        remove_astronaut = self.astronaut_repository.find_by_name(name)
        if remove_astronaut is None:
            raise Exception(f'Astronaut {name} doesn`t exist')
        self.astronaut_repository.remove(remove_astronaut)
        return f"Astronaut {remove_astronaut} retired"

    def recharged_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception(f'Invalid planet name!')

        astronauts = self.astronaut_repository.find_most_suitable(5, 30)
        if len(astronauts) == 0:
            raise Exception(f'You need at least ')
        for astronaut in astronauts:
            if len(planet.item) == 0:
                break
            count = 0
            while astronaut.oxygen > 0 or len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
                count += 1
        if len(planet.items) == 0:
            self.successful_mission += 1
            return f"Planet: {planet_name} was explored. {astronauts} astronauts participated in collecting items."
        else:
            self.failed_mission += 1
            return f'Mission is not completed.'

    def report(self):
        result = f'{self.successful_mission} successful missions!' + '\n'
        result += f'{self.failed_mission} missions were not completed!' + '\n'
        result += "Astronauts info:+'\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += str(astronaut) + '\n'

        return result.strip()

    def __create_astronaut(self, astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        if astronaut_type == Biologist.__name__:
            return Meteorologist(name)
        if astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)
        raise Exception("Astronaut type is not valid!")
