import unittest

from movie_app_unittest.plantation import Plantation


class PlantationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(2)
        self.plantation.plants = {"a": ["rose", "lale"], "b": ["rose", "lale"]}
        self.plantation.workers = ['a', 'b']

    def test_correct_initialization(self):
        self.assertEqual(self.plantation.size, 2)
        self.assertEqual(self.plantation.plants, {"a": ["rose", "lale"], "b": ["rose", "lale"]})
        self.assertEqual(self.plantation.workers, ['a', 'b'])

    def test_wrong_size(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -1
        self.assertEqual(str(ex.exception), "Size must be positive number!")

    def test_hire_worker_wrong(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("a")
        self.assertEqual(str(ex.exception), "Worker already hired!")

    def test_hire_correctly(self):
        result = self.plantation.hire_worker("c")
        self.assertEqual(result, f"c successfully hired.")
        self.assertEqual(self.plantation.workers, ['a', 'b', 'c'])

    def test_len(self):
        result = len(self.plantation)
        self.assertEqual(result, 4)

    def test_wrong_planting(self):
        plant = Plantation(4)
        plant.plants = {"b": ["rose", "lale"], "c": ["rose", "lale"]}
        plant.workers = ['a', 'b', 'c']

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("c", "something")
        self.assertEqual(str(ex.exception), "Worker with name c is not hired!")

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("a", "something")
        self.assertEqual(str(ex.exception), "The plantation is full!")

        with self.assertRaises(ValueError) as ex:
            plant.planting("a", "something")
        self.assertEqual(str(ex.exception), "The plantation is full!")

    def test_correct_planting_existing_worker(self):
        plant = Plantation(5)
        plant.plants = {"a": ["rose", "lale"], "b": ["rose", "lale"]}
        plant.workers = ['a', 'b']
        result = plant.planting("a", "something")
        self.assertEqual(result, "a planted something.")
        self.assertEqual(plant.plants, {"a": ["rose", "lale", "something"], "b": ["rose", "lale"]})

    def test_correct_planting_new_key_worker(self):
        plant = Plantation(5)
        plant.plants = {"b": ["rose", "lale"], "c": ["rose", "lale"]}
        plant.workers = ['a', 'b', 'c']

        result = plant.planting("a", "something")
        self.assertEqual(result, "a planted it's first something.")
        self.assertEqual(plant.plants, {"a": ["something"], "b": ["rose", "lale"], "c": ["rose", "lale"]})

    def test_str_representation(self):
        result = str(self.plantation)
        self.assertEqual(result, "Plantation size: 2\na, b\na planted: rose, lale\nb planted: rose, lale")

    def test_repr_correctly(self):
        result = self.plantation.__repr__()
        self.assertEqual(result, "Size: 2\nWorkers: a, b")


if __name__ == "__main__":
    unittest.main()
