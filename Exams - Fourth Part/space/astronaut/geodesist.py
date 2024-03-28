from space.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 50)

    def breathe(self):
        self.oxygen -= 10
