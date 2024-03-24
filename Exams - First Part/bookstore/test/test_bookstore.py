from bookstore.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(100)

    def test_correct_initialization(self):
        self.assertEqual(self.bookstore.books_limit, 100)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 0)

    def test_books_limit(self):
        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = 0

        self.assertEqual(str(ex.exception), "Books limit of 0 is not valid")

        with self.assertRaises(ValueError) as ex:
            self.bookstore.books_limit = -1

        self.assertEqual(str(ex.exception), "Books limit of -1 is not valid")

    def test_len_bookstore(self):
        bookstore = Bookstore(200)
        bookstore.availability_in_store_by_book_titles = {'some book': 5, 'other book': 4}
        result = len(bookstore)
        self.assertEqual(result, 9)

    def test_len_bookstore_without_any_books_initially(self):
        bookstore = Bookstore(200)
        result = len(bookstore)
        self.assertEqual(result, 0)

    def test_receive_book_reached_book_limit(self):
        bookstore = Bookstore(50)
        bookstore.availability_in_store_by_book_titles = {'some book': 20, 'other book': 20}
        with self.assertRaises(Exception) as ex:
            bookstore.receive_book("whatever", 20)

        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_correcty(self):
        bookstore = Bookstore(100)
        bookstore.availability_in_store_by_book_titles = {'some book': 20, 'other book': 20}
        result = bookstore.receive_book('book_one', 2)
        self.assertEqual(bookstore.availability_in_store_by_book_titles,
                         {'some book': 20, 'other book': 20, 'book_one': 2})
        self.assertEqual(result, "2 copies of book_one are available in the bookstore.")

        another_result = bookstore.receive_book('book_one', 2)
        self.assertEqual(bookstore.availability_in_store_by_book_titles,
                         {'some book': 20, 'other book': 20, 'book_one': 4})
        self.assertEqual(another_result, "4 copies of book_one are available in the bookstore.")
        total_number_of_books = len(bookstore)
        self.assertEqual(total_number_of_books, 44)

    def test_sell_book_book_doesnt_exists(self):
        bookstore = Bookstore(100)
        bookstore.availability_in_store_by_book_titles = {'some book': 20, 'other book': 20}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book('title', 5)
        self.assertEqual(str(ex.exception), "Book title doesn't exist!")

    def test_sell_all_books(self):
        bookstore = Bookstore(100)
        bookstore.availability_in_store_by_book_titles = {'some book': 20}
        result = bookstore.sell_book('some book', 20)
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {'some book': 0})
        self.assertEqual(bookstore._Bookstore__total_sold_books, 20)
        self.assertEqual(result, 'Sold 20 copies of some book')
        total_number_of_books = len(bookstore)
        self.assertEqual(total_number_of_books, 0)

    def test_sell_book_less_copies(self):
        bookstore = Bookstore(100)
        bookstore.availability_in_store_by_book_titles = {'some book': 5, 'other book': 20}
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book('some book', 10)
        self.assertEqual(str(ex.exception), "some book has not enough copies to sell. Left: 5")

    def test_sell_book_successfully(self):
        bookstore = Bookstore(100)
        bookstore.availability_in_store_by_book_titles = {'some book': 20, 'other book': 20}
        result = bookstore.sell_book('some book', 10)
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {'some book': 10, 'other book': 20})
        self.assertEqual(bookstore._Bookstore__total_sold_books, 10)
        self.assertEqual(result, 'Sold 10 copies of some book')

    def test_sell_zero_books(self):
        bookstore = Bookstore(100)
        bookstore.availability_in_store_by_book_titles = {'some book': 20, 'other book': 20}
        result = bookstore.sell_book('some book', 0)
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {'some book': 20, 'other book': 20})
        self.assertEqual(bookstore._Bookstore__total_sold_books, 0)
        self.assertEqual(result, 'Sold 0 copies of some book')

    def test_string_representation(self):
        bookstore = Bookstore(100)
        bookstore.availability_in_store_by_book_titles = {'some book': 20, 'other book': 20}
        bookstore.sell_book('some book', 10)
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {'some book': 10, 'other book': 20})
        self.assertEqual(bookstore._Bookstore__total_sold_books, 10)
        self.assertEqual(len(bookstore), 30)
        result = str(bookstore)
        self.assertEqual(result,
                         'Total sold books: 10\nCurrent availability: 30\n - some book: 10 copies\n - other book: 20 copies')


if __name__ == "__main__":
    unittest.main()
