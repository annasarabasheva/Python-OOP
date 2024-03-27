from musician_band.band import Band
from musician_band.band_members.drummer import Drummer
from musician_band.band_members.guitarist import Guitarist
from musician_band.band_members.singer import Singer
from musician_band.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")
        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        if musician_type == 'Guitarist':
            musician = Guitarist(name, age)
            self.musicians.append(musician)
        elif musician_type == 'Drummer':
            musician = Drummer(name, age)
            self.musicians.append(musician)
        elif musician_type == 'Singer':
            musician = Singer(name, age)
            self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        all_musicians_names = [m.name for m in self.musicians]
        all_bands_names = [b.name for b in self.bands]
        if musician_name not in all_musicians_names:
            raise Exception(f"{musician_name} isn't a musician!")
        elif band_name not in all_bands_names:
            raise Exception(f"{band_name} isn't a band!")
        musician = [m for m in self.musicians if m.name == musician_name][0]
        band = [b for b in self.bands if b.name == band_name][0]
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        all_bands_names = [b.name for b in self.bands]
        if band_name not in all_bands_names:
            raise Exception(f"{band_name} isn't a band!")
        band = [b for b in self.bands if b.name == band_name][0]
        all_musicians_names_in_band = [m.name for m in band.members]
        if musician_name not in all_musicians_names_in_band:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        musician = [m for m in band.members if m.name == musician_name][0]
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = [c for c in self.concerts if c.place == concert_place][0]
        band = [b for b in self.bands if b.name == band_name][0]
        band_members = {"Singer": 0, "Drummer": 0, "Guitarist": 0}
        for member in band.members:
            band_members[member.__class__.__name__] += 1
        for value in band_members.values():
            if not value:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        drummer = [m for m in band.members if m.__class__.__name__ == "Drummer"][0]
        singer = [m for m in band.members if m.__class__.__name__ == "Singer"][0]
        guitarist = [m for m in band.members if m.__class__.__name__ == "Guitarist"][0]
        if concert.genre == 'Rock':
            needed_drummer_skill = "play the drums with drumsticks"
            needed_singer_skill = "sing high pitch notes"
            needed_guitarist_skill = "play rock"

            if (needed_drummer_skill not in drummer.skills) or (needed_singer_skill not in singer.skills) or (
                    needed_guitarist_skill not in guitarist.skills):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            needed_drummer_skill = "play the drums with drumsticks"
            needed_singer_skill = "sing low pitch notes"
            needed_guitarist_skill = "play metal"

            if (needed_drummer_skill not in drummer.skills) or (needed_singer_skill not in singer.skills) or (
                    needed_guitarist_skill not in guitarist.skills):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            needed_drummer_skill = "play the drums with drum brushes"
            needed_singer_skill = "sing high pitch notes"
            needed_another_singer_skill = "sing low pitch notes"
            needed_guitarist_skill = "play jazz"

            if (needed_drummer_skill not in drummer.skills) or (
                    needed_singer_skill not in singer.skills or needed_another_singer_skill not in singer.skills) or (
                    needed_guitarist_skill not in guitarist.skills):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
