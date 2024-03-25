from horse_race.horse_race import HorseRace
from horse_race.horse_specification.appaloosa import Appaloosa
from horse_race.horse_specification.thoroughbred import Thoroughbred
from horse_race.jockey import Jockey


class HorseRaceApp:
    all_types_of_races = {"Winter": 0, "Spring": 0, "Autumn": 0, "Summer": 0}

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."
        elif horse_type == "Thoroughbred":
            horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race, times in HorseRaceApp.all_types_of_races.items():
            if race == race_type:
                if times == 0:
                    HorseRaceApp.all_types_of_races[race_type] += 1
                    race = HorseRace(race_type)
                    self.horse_races.append(race)
                    return f"Race {race_type} is created."
                else:
                    raise Exception(f"Race {race_type} has been already created!")

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey_list = []
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                jockey_list.append(jockey)
        if not jockey_list:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = jockey_list[0]

        horse_list = []
        for horse in self.horses[::-1]:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                horse_list.append(horse)
                break
        if not horse_list:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        horse = horse_list[0]
        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = []
        for race in self.horse_races:
            if race.race_type == race_type:
                horse_race.append(race)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        race = horse_race[0]
        jockey_list = []
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                jockey_list.append(jockey)
        if not jockey_list:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        jockey = jockey_list[0]
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race_list = []
        for race in self.horse_races:
            if race.race_type == race_type:
                horse_race_list.append(race)
        if not horse_race_list:
            raise Exception(f"Race {race_type} could not be found!")
        race = horse_race_list[0]
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = None
        horse_winner = None
        highest_speed = 0
        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner = jockey
                horse_winner = jockey.horse

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner.name}! Winner's horse: {horse_winner.name}."
