class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False



import unittest

class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("name")

    def test_correct_initialization(self):
        self.assertEqual(self.cat.name, "name")
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_cat_already_fed_and_eats(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_feeding_cat_correctly(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(self.cat.size, 1)

    def test_sleeping_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_sleeping_correctly(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(self.cat.size, 1)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()