from meal_menu_unfinished.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_correct_initialization(self):
        self.assertEqual(self.toy.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_shelf_doesnt_exists(self):
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('H', 'hippo')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_toy_already_exists(self):
        self.toy.add_toy('B', 'banana')
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('B', 'banana')
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_not_none(self):
        self.toy.add_toy('G', 'giraffe')
        with self.assertRaises(Exception) as ex:
            self.toy.add_toy('G', 'notNone')
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_correctly(self):

        result = self.toy.add_toy('A', 'apple')
        self.assertEqual(self.toy.toy_shelf, {
            "A": 'apple',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })
        self.assertEqual(result, 'Toy:apple placed successfully!')

    def test_remove_toy_shelf_doesnt_exists(self):
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('H', 'hippo')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_toy_doesnt_exists(self):
        self.toy.add_toy('A', 'angel')
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy('A', 'ananas')
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_correctly(self):
        self.toy.add_toy('A', 'angel')
        result = self.toy.remove_toy('A', 'angel')
        self.assertEqual(self.toy.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })
        self.assertEqual(result, "Remove toy:angel successfully!")


if __name__ == "__main__":
    unittest.main()