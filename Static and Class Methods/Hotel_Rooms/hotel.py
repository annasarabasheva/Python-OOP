from Hotel_Rooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if room.capacity >= people and not room.is_taken:
                    room.is_taken = True
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken:
                    room.is_taken = False
                    self.guests = 0

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        free_rooms = []
        taken_rooms = []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(room.number)
            else:
                free_rooms.append(room.number)
        result += f"Free rooms: {', '.join([str(el) for el in free_rooms])}\nTaken rooms: {', '.join([str(el) for el in taken_rooms])}"
        return result










