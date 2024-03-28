from space.astronaut.biologist import Biologist
from space.astronaut.geodesist import Geodesist
from space.astronaut.meteorologist import Meteorologist
from space.planet.planet import Planet


class SpaceStation:
    def __init__(self):
        self.planet_repository = []
        self.astronaut_repository = []

    def add_astronaut(self, astronaut_type: str, name: str):
        for astronaut in self.astronaut_repository:
            if astronaut.name == name:
                return f"{name} is already added."
        if astronaut_type == 'Biologist':
            astronaut = Biologist(name)
            self.astronaut_repository.append(astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        elif astronaut_type == 'Geodesist':
            astronaut = Geodesist(name)
            self.astronaut_repository.append(astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        elif astronaut_type == 'Meteorologist':
            astronaut = Meteorologist(name)
            self.astronaut_repository.append(astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):
        for planet in self.planet_repository:
            if planet.name == name:
                return f"{name} is already added."
        planet = Planet(name)










