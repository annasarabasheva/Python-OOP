from rename.library import Library
import unittest


class TestLibrary(unittest.TestCase):

    def setUp(self) -> None:
        self.library = Library('name')

    def test_correct_initialization(self):
        self.assertEqual(self.library.name, 'name')
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_name_initialization(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual(str(ex.exception), "Name cannot be empty string!")

    def test_add_book(self):
        self.library.books_by_authors = {'author_one': ['title_one'], 'author_two': ['title_two']}
        self.library.add_book('author_three', 'title_three')
        self.assertEqual(self.library.books_by_authors, {'author_one': ['title_one'], 'author_two': ['title_two'], 'author_three': ['title_three']})

        self.library.add_book('author_two', 'some_title')
        self.assertEqual(self.library.books_by_authors, {'author_one': ['title_one'], 'author_two': ['title_two', 'some_title'], 'author_three': ['title_three']})

        self.library.add_book('author_one', 'title_one')
        self.assertEqual(self.library.books_by_authors, {'author_one': ['title_one'], 'author_two': ['title_two', 'some_title'], 'author_three': ['title_three']})

    def test_add_reader(self):
        self.library.readers = {'name': []}
        result = self.library.add_reader('name')
        self.assertEqual(result, "name is already registered in the name library.")

        self.library.add_reader('another_name')
        self.assertEqual(self.library.readers, {'name': [], 'another_name': []})

    def test_rent_book(self):
        self.library.books_by_authors = {'author_one': ['title_one'], 'author_two': ['title_two']}
        self.library.readers = {'name': [], 'another_name': []}
        result = self.library.rent_book('bla bla name', 'author_one', 'title_one')
        self.assertEqual(result, "bla bla name is not registered in the name Library.")

        result_two = self.library.rent_book('name', 'author_four', 'title_one')
        self.assertEqual(result_two, "name Library does not have any author_four's books.")

        result_three = self.library.rent_book('name', 'author_one', 'title_two')
        self.assertEqual(result_three, """name Library does not have author_one's "title_two".""")

        self.library.rent_book('name', 'author_one', 'title_one')
        self.assertEqual(self.library.readers,  {'name': [{'author_one': 'title_one'}], 'another_name': []})
        self.assertEqual(self.library.books_by_authors, {'author_one': [], 'author_two': ['title_two']})

if __name__ == '__main__':
    unittest.main()






