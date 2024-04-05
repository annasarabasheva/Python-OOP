class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

car = Car("a", "b", 1, 4)
car.make = ""
print(car)

import unittest

class TestCar(unittest.TestCase):
    def setUp(self):
        # Create a Car instance with initial values
        self.car = Car("Toyota", "Camry", 7.5, 50)

    def test_make_model_properties(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "Camry")

        with self.assertRaises(Exception):
            # Test setting empty make and model
            self.car.make = ""
        with self.assertRaises(Exception):
            self.car.model = None

    def test_fuel_consumption_property(self):
        self.assertEqual(self.car.fuel_consumption, 7.5)

        with self.assertRaises(Exception):
            # Test setting zero or negative fuel consumption
            self.car.fuel_consumption = -5
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0

    def test_fuel_capacity_property(self):
        self.assertEqual(self.car.fuel_capacity, 50)

        with self.assertRaises(Exception):
            # Test setting zero or negative fuel capacity
            self.car.fuel_capacity = -10
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

    def test_fuel_amount_property(self):
        self.assertEqual(self.car.fuel_amount, 0)

        with self.assertRaises(Exception):
            # Test setting negative fuel amount
            self.car.fuel_amount = -10

    def test_refuel_method(self):
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_amount, 20)

        # Refueling above the fuel capacity should be capped
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, 50)

        with self.assertRaises(Exception):
            # Test refueling with zero or negative fuel
            self.car.refuel(-5)
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_drive_method(self):
        # Start with some fuel
        self.car.refuel(40)

        # Drive within available fuel range
        self.car.drive(300)
        self.assertEqual(self.car.fuel_amount, 40 - (300 / 100) * 7.5)

        # Try to drive beyond available fuel range
        with self.assertRaises(Exception):
            self.car.drive(1000)

if __name__ == "__main__":
    unittest.main()
