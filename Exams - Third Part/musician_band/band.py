class Band:
    def __init__(self, name):
        self.name = name
        self.members = []  # (musician_band objects) of the band

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Band name should contain at least one character!")
        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."