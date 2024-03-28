from truck_driver.truck_driver import TruckDriver
import unittest

class TruckDriverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver("stancho", 100)
        self.truck_driver.available_cargos = {"beer": 5}
        self.truck_driver.earned_money = 0
        self.truck_driver.miles = 0

    def test_correct_initialization(self):
        self.assertEqual(self.truck_driver.name, "stancho")
        self.assertEqual(self.truck_driver.money_per_mile, 100)
        self.assertEqual(self.truck_driver.available_cargos, {"beer": 5})
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_wrong_earned_money(self):
        with self.assertRaises(ValueError) as ex:
            self.truck_driver.earned_money = -1

        self.assertEqual(str(ex.exception), "stancho went bankrupt.")

    def test_bankrupt(self):
        self.truck_driver.money_per_mile = 0.01
        self.truck_driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"stancho went bankrupt.")

    def test_add_cargo_with_existing_location(self):
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("beer", 10)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_correctly(self):
        result = self.truck_driver.add_cargo_offer("something", 10)
        self.assertEqual(self.truck_driver.available_cargos, {"beer": 5, "something": 10})
        self.assertEqual(result, "Cargo for 10 to something was added as an offer.")

    def test_drive_best_cargo_offer(self):
        driver = TruckDriver("name", 0.5)
        self.assertEqual(driver.drive_best_cargo_offer(), "There are no offers available.")

        driver.add_cargo_offer("Destination A", 100)
        driver.add_cargo_offer("Destination B", 200)
        driver.add_cargo_offer("Destination C", 150)

        self.assertEqual(driver.drive_best_cargo_offer(), "name is driving 200 to Destination B.")
        self.assertEqual(driver.earned_money, 100.0)
        self.assertEqual(driver.miles, 200)

    def test_drive_cargo_offer_more_than_250_miles(self):
        driver = TruckDriver("name", 0.5)
        driver.add_cargo_offer("Destination B", 250)

        self.assertEqual(driver.drive_best_cargo_offer(), "name is driving 250 to Destination B.")
        self.assertEqual(driver.earned_money, 105.0)
        self.assertEqual(driver.miles, 250)

    def test_drive_going_into_bankruptcy(self):
        driver = TruckDriver("name", 0.5)
        driver.add_cargo_offer("Destination B", 10000)

        with self.assertRaises(ValueError) as ve:
            driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"name went bankrupt.")

    def test_check_for_activities_without_bankruptcy(self):
        driver = TruckDriver("name", 0.5)
        driver.earned_money = 100000
        driver.check_for_activities(10000)
        self.assertEqual(driver.earned_money,88250)

    def test_check_for_activities_into_bankruptcy(self):
        driver = TruckDriver("name", 0.5)
        driver.earned_money = 4000
        with self.assertRaises(ValueError) as ve:
            driver.check_for_activities(10000)

        self.assertEqual(str(ve.exception), f"name went bankrupt.")

    def test_eat(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.eat(250)
        self.truck_driver.eat(500)

        self.assertEqual(self.truck_driver.earned_money, 60)

    def test_sleep(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.sleep(1000)
        self.truck_driver.sleep(2000)

        self.assertEqual(self.truck_driver.earned_money, 10)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 2000

        self.truck_driver.pump_gas(1500)
        self.truck_driver.pump_gas(3000)

        self.assertEqual(self.truck_driver.earned_money, 1000)


    def test_repair_truck(self):
        self.truck_driver.earned_money = 16000

        self.truck_driver.repair_truck(10000)
        self.truck_driver.repair_truck(20000)

        self.assertEqual(self.truck_driver.earned_money, 1000)

    def test_repr(self):
        driver = TruckDriver("name", 0.5)
        self.assertEqual(repr(driver), "name has 0 miles behind his back.")


if __name__ == "__main__":
    unittest.main()


