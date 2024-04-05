import unittest

from movie_app.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Perry", "platypus", "test_sound")

    def test_initialization(self):
        self.assertEqual(self.mammal.name, "Perry")
        self.assertEqual(self.mammal.type, "platypus")
        self.assertEqual(self.mammal.sound, "test_sound")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual(result, "Perry makes test_sound")

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual(result, "Perry is of type platypus")


if __name__ == "__main__":
    unittest.main()