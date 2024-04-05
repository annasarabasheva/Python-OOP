import unittest

from movie_app.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100.10, 100.50)

    def test_class_initialization(self):
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_initialization(self):
        self.assertEqual(self.vehicle.fuel, 100.10)
        self.assertEqual(self.vehicle.horse_power, 100.50)
        self.assertEqual(self.vehicle.capacity, 100.10)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_driving_with_less_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_driving_with_enough_fuel(self):
        self.vehicle.drive(60)
        self.assertEqual(self.vehicle.fuel, 25.099999999999994)

        self.vehicle.drive(20)
        self.assertEqual(self.vehicle.fuel, 0.09999999999999432)

    def test_refuel_but_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_correctly(self):
        self.vehicle.fuel = 50.50
        self.vehicle.refuel(20)
        self.assertEqual(self.vehicle.fuel, 70.50)

        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 80.50)

    def test_string_representation(self):
        result = str(self.vehicle)

        self.assertEqual(result, "The vehicle has 100.5 horse power with 100.1 fuel left and 1.25 fuel consumption")