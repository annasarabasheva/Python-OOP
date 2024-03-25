from movie_app.movie import Movie
import unittest


class MovieTest(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Titanic", 1997, 8.6)
        self.movie.actors = ["Robert Downey Jr."]

    def test_correct_initialization(self):
        self.assertEqual(self.movie.name, "Titanic")
        self.assertEqual(self.movie.year, 1997)
        self.assertEqual(self.movie.rating, 8.6)
        self.assertEqual(self.movie.actors, ["Robert Downey Jr."])

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertEqual(str(ex.exception), "Name cannot be an empty string!")

    def test_invalid_year(self):
        with self.assertRaises(ValueError)as ex:
            self.movie.year = 1500
        self.assertEqual(str(ex.exception), "Year is not valid!")

    def test_add_actor(self):
        self.movie.add_actor("Scarlett Johansson")
        self.assertEqual(
            self.movie.actors,
            ["Robert Downey Jr.", "Scarlett Johansson"]
        )
        self.movie.add_actor("Robert Downey Jr.")
        result = self.movie.add_actor("Robert Downey Jr.")
        self.assertEqual(result, "Robert Downey Jr. is already added in the list of actors!")


    def test_comparison(self):
        new_movie = Movie("Batman", 2008, 9.0)
        other_movie = Movie("Iron Man", 2008, 7.9)
        other_movie_with_same_rating = Movie("Iron Man 12", 2010, 7.9)
        self.assertGreater(self.movie, other_movie)
        self.assertEqual(str(self.movie > other_movie), '"Titanic" is better than "Iron Man"')
        self.assertEqual(str(other_movie > self.movie), '"Titanic" is better than "Iron Man"')
        self.assertEqual(str(new_movie > self.movie), '"Batman" is better than "Titanic"')
        self.assertEqual(str(other_movie > other_movie_with_same_rating), '"Iron Man 12" is better than "Iron Man"')

    def test_representation(self):
        result = self.movie.__repr__()
        self.assertEqual(result, f"Name: Titanic\nYear of Release: 1997\nRating: 8.60\nCast: Robert Downey Jr.")


if __name__ == "__main__":
    unittest.main()