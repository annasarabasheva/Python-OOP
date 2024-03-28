from robot_service.tennis_player import TennisPlayer
import unittest


class TennisPlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("name", 22, 12)
        self.tennis_player.wins = ["something"]

    def test_correct_initialization(self):
        self.assertEqual(self.tennis_player.name, "name")
        self.assertEqual(self.tennis_player.age, 22)
        self.assertEqual(self.tennis_player.points, 12)
        self.assertEqual(self.tennis_player.wins, ["something"])

    def test_wrong_name(self):
        with self.assertRaises(ValueError) as ex:
            self.tennis_player.name = "a"
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_wrong_name_with_two_symbols(self):
        with self.assertRaises(ValueError) as ex:
            self.tennis_player.name = "aa"
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_wrong_age(self):
        with self.assertRaises(ValueError) as ex:
            self.tennis_player.age = 16
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_tournament_exists(self):
        result = self.tennis_player.add_new_win("something")
        self.assertEqual(result, "something has been already added to the list of wins!")

    def test_add_new_win_tournament_doesnt_exists(self):
        self.tennis_player.add_new_win("another")
        self.assertEqual(self.tennis_player.wins, ["something", "another"])

    def test_other_greater_than_self(self):
        other = TennisPlayer("gaga", 23, 22)
        result = self.tennis_player < other
        self.assertEqual(result, "gaga is a top seeded player and he/she is better than name")

    def test_other_lower_than_self(self):
        other = TennisPlayer("gaga", 23, 10)
        result = self.tennis_player < other
        self.assertEqual(result, "name is a better player than gaga")

    # def test_other_equal_than_self(self):
    #     other = TennisPlayer("gaga", 23, 12)
    #     result = self.tennis_player < other
    #     self.assertEqual(result, "name is a better player than gaga")

    def test_string_representation(self):
        self.tennis_player.wins = ["something", "babai"]
        result = str(self.tennis_player)
        self.assertEqual(result, "Tennis Player: name\nAge: 22\nPoints: 12.0\nTournaments won: something, babai")


if __name__ == "__main__":
    unittest.main()
