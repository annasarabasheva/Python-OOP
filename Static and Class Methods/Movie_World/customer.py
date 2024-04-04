
from Movie_World.dvd import DVD
class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = [] # DVD instances

    def __repr__(self):
        dvd_names = []
        for dvd in self.rented_dvds:
            dvd_names.append(dvd.name)
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(dvd_names)})"
