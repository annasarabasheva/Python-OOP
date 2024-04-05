class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)
import unittest

class TestIntegerList(unittest.TestCase):
    def setUp(self):
        # Create an IntegerList instance with some initial data
        self.integer_list = IntegerList(1, 2, 3, 4, 5)

    def test_get_data(self):
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4, 5])

    def test_add_valid_element(self):
        self.assertEqual(self.integer_list.add(6), [1, 2, 3, 4, 5, 6])

    def test_add_invalid_element(self):
        with self.assertRaises(ValueError):
            self.integer_list.add("not_an_integer")

    def test_remove_index_valid(self):
        self.assertEqual(self.integer_list.remove_index(2), 3)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 4, 5])

    def test_remove_index_invalid(self):
        with self.assertRaises(IndexError):
            self.integer_list.remove_index(10)

    def test_get_valid_index(self):
        self.assertEqual(self.integer_list.get(3), 4)

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError):
            self.integer_list.get(10)

    def test_insert_valid(self):
        self.integer_list.insert(2, 100)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 100, 3, 4, 5])

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.integer_list.insert(10, 100)

    def test_insert_invalid_element(self):
        with self.assertRaises(ValueError):
            self.integer_list.insert(2, "not_an_integer")

    def test_get_biggest(self):
        self.assertEqual(self.integer_list.get_biggest(), 5)

    def test_get_index(self):
        self.assertEqual(self.integer_list.get_index(3), 2)

    def test_get_index_nonexistent_element(self):
        with self.assertRaises(ValueError):
            self.integer_list.get_index(10)

if __name__ == "__main__":
    unittest.main()


