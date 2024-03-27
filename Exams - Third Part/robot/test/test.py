from robot.robot import Robot
import unittest

class RobotTest(unittest.TestCase):
    def setUp(self) -> None:
        self.robot = Robot("123", "Humanoids", 100, 100)
        self.hardware_upgrades = []
        self.software_upgrades = []
        Robot.ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
        Robot.PRICE_INCREMENT = 1.5

    def test_correct_initialization(self):
        self.assertEqual(self.robot.robot_id, "123")
        self.assertEqual(self.robot.category, "Humanoids")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 100)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_class_attributes(self):
        self.assertEqual(Robot.ALLOWED_CATEGORIES, ['Military', 'Education', 'Entertainment', 'Humanoids'])
        self.assertEqual(Robot.PRICE_INCREMENT, 1.5)

    def test_wrong_category(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "a"
        self.assertEqual(str(ex.exception), "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_wrong_price(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = -1
        self.assertEqual(str(ex.exception), "Price cannot be negative!")

    def test_existing_upgrade(self):
        self.robot.hardware_upgrades = ["something"]
        result = self.robot.upgrade("something", 100)
        self.assertEqual(result, "Robot 123 was not upgraded.")

    def test_upgrade_correctly(self):
        result = self.robot.upgrade("something", 100)
        self.assertEqual(self.robot.hardware_upgrades, ["something"])
        self.assertEqual(self.robot.price, 250)
        self.assertEqual(result, "Robot 123 was upgraded with something.")

    def test_successful_update(self):
        result = self.robot.update(1.2, 30)
        self.assertEqual(result, "Robot 123 was updated to version 1.2.")
        self.assertEqual(self.robot.available_capacity, 70)
        self.assertEqual(self.robot.software_updates, [1.2])

    def test_failed_update_capacity(self):
        result = self.robot.update(1.3, 120)
        self.assertEqual(result, "Robot 123 was not updated.")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.software_updates, [])

    def test_failed_update_version(self):
        self.robot.update(1.2, 30)
        result = self.robot.update(1.1, 20)
        self.assertEqual(result, "Robot 123 was not updated.")
        # The available capacity should not change as the update failed
        self.assertEqual(self.robot.available_capacity, 70)
        self.assertEqual(self.robot.software_updates, [1.2])

    def test_update_version_comparison(self):
        result_one = self.robot.update(1.2, 30)
        self.assertEqual(result_one, "Robot 123 was updated to version 1.2.")
        result_two = self.robot.update(1.3, 20)
        self.assertEqual(result_two, "Robot 123 was updated to version 1.3.")
        self.assertEqual(self.robot.available_capacity, 50)
        self.assertEqual(self.robot.software_updates, [1.2, 1.3])

    def test_price_comparison_self_is_cheaper(self):
        other = Robot("456", "Military", 100, 200)
        self.assertEqual(self.robot > other, "Robot with ID 123 is cheaper than Robot with ID 456.")

    def test_self_is_more_expensive(self):
        other = Robot("456", "Military", 100, 50)
        self.assertEqual(self.robot > other, "Robot with ID 123 is more expensive than Robot with ID 456.")

    def test_equal(self):
        other = Robot("456", "Military", 100, 100)
        self.assertEqual(self.robot > other, "Robot with ID 123 costs equal to Robot with ID 456.")


if __name__ == "__main__":
    unittest.main()