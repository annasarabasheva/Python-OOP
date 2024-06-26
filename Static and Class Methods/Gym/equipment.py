class Equipment:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.id
        Equipment.id += 1

    def get_next_id(self):
        return self.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.id

