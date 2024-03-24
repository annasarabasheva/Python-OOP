from car_race.car.muscle_car import MuscleCar
from car_race.car.sports_car import SportsCar
from car_race.driver import Driver
from car_race.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")
        if car_type == "MuscleCar":
            car = MuscleCar(model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."
        elif car_type == "SportsCar":
            car = SportsCar(model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        drivers_names = [driver.name for driver in self.drivers]
        if driver_name not in drivers_names:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = [d for d in self.drivers if d.name == driver_name][0]
        car_list = []
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                car_list.append(car)
                break
        if not car_list:
            raise Exception(f"Car {car_type} could not be found!")
        car = car_list[0]
        if driver.car is not None:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_car.model} to {car.model}."
        driver.car = car
        car.is_taken = True
        return f"Driver {driver.name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race_list = []
        for race in self.races:
            if race.name == race_name:
                race_list.append(race)
        if not race_list:
            raise Exception(f"Race {race_name} could not be found!")
        race = race_list[0]
        driver_list = []
        for driver in self.drivers:
            if driver.name == driver_name:
                driver_list.append(driver)
        if not driver_list:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = driver_list[0]
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race_list = []
        for race in self.races:
            if race.name == race_name:
                race_list.append(race)
        if not race_list:
            raise Exception(f"Race {race_name} could not be found!")
        race = race_list[0]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        speed_limits = []
        for driver in race.drivers:
            speed_limits.append(driver.car.speed_limit)
        speed_limits.sort()
        highest_three = speed_limits[-3:]
        third_place_driver = None
        second_place_driver = None
        first_place_driver = None
        for driver in race.drivers:
            if driver.car.speed_limit == highest_three[0]:
                third_place_driver = driver
                driver.number_of_wins += 1
            elif driver.car.speed_limit == highest_three[1]:
                second_place_driver = driver
                driver.number_of_wins += 1
            elif driver.car.speed_limit == highest_three[2]:
                first_place_driver = driver
                driver.number_of_wins += 1

        result = f"Driver {first_place_driver.name} wins the {race_name} race with a speed of {first_place_driver.car.speed_limit}.\n"
        result += f"Driver {second_place_driver.name} wins the {race_name} race with a speed of {second_place_driver.car.speed_limit}.\n"
        result += f"Driver {third_place_driver.name} wins the {race_name} race with a speed of {third_place_driver.car.speed_limit}."
        return result







