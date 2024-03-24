from Second_Hand_Car.second_hand_car import SecondHandCar
import unittest


class TestSecondHandCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar('model', 'type', 1000, 1000.0)

    def test_correct_initialization(self):
        self.assertEqual(self.car.model, 'model')
        self.assertEqual(self.car.car_type, 'type')
        self.assertEqual(self.car.mileage, 1000)
        self.assertEqual(self.car.price, 1000.0)
        self.assertEqual(self.car.repairs, [])

    def test_price(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1.0
        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')

        with self.assertRaises(ValueError) as ex:
            self.car.price = 0.0
        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')

    def test_mileage(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 99
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price_with_higher_new_price_and_equal_new_price(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(2000.0)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(1000.0)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_set_promotional_price_without_error(self):
        result = self.car.set_promotional_price(500.0)
        self.assertEqual(self.car.price, 500.0)
        self.assertEqual(result, 'The promotional price has been successfully set.')

    def test_need_repair_repair_is_impossible(self):
        result = self.car.need_repair(600.0, 'lights changed')
        self.assertEqual(result, 'Repair is impossible!')

    def test_need_repair_possible(self):
        result = self.car.need_repair(400.0, 'lights changed')
        self.assertEqual(self.car.price, 1400.0)
        self.assertEqual(self.car.repairs, ['lights changed'])
        self.assertEqual(result, 'Price has been increased due to repair charges.')

    def test_compare_cars_when_car_type_is_different(self):
        other_car = SecondHandCar('some model', 'other type', 500, 2000.0)
        result = self.car > other_car
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_compare_cars_when_car_type_is_same(self):
        other_car = SecondHandCar('some model', 'type', 500, 2000.0)
        result = self.car > other_car
        self.assertFalse(result)

        another_car = SecondHandCar('another model', 'type', 800, 700.0)
        another_result = self.car > another_car
        self.assertTrue(another_result)

    def test_string_representation_when_number_of_repairs_is_zero(self):
        result = str(self.car)
        self.assertEqual(result, "Model model | Type type | Milage 1000km\nCurrent price: 1000.00 | Number of Repairs: 0")

    def test_string_representation_when_number_of_repairs_is_more_than_zero(self):
        self.car.repairs = ['repair_one', 'repair_two', 'repair_three']
        self.assertEqual(self.car.repairs, ['repair_one', 'repair_two', 'repair_three'])
        result = str(self.car)
        self.assertEqual(result, "Model model | Type type | Milage 1000km\nCurrent price: 1000.00 | Number of Repairs: 3")


if __name__ == '__main__':
    unittest.main()






