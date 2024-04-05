import unittest

from movie_app.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("username", 5, 100.10, 20.5)

    def test_correct_initialization(self):
        self.assertEqual(self.hero.username, "username")
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 100.10)
        self.assertEqual(self.hero.damage, 20.5)

    def test_string_representation(self):
        result = str(self.hero)
        self.assertEqual(result, f"Hero username: 5 lvl\nHealth: 100.1\nDamage: 20.5\n")

    def test_battle_with_same_object(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_with_zero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(Hero("a", 4, 90.5, 25.5))
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_with_minus_health(self):
        self.hero.health = -1
        enemy_hero = Hero("a", 4, 90.5, 25.5)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_zero_health(self):
        enemy_hero = Hero("a", 4, 0, 25.5)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception), "You cannot fight a. He needs to rest")

    def test_battle_enemy_minus_health(self):
        enemy_hero = Hero("a", 4, -1, 25.5)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception), "You cannot fight a. He needs to rest")

    def test_battle_health_equals_zero_for_hero_and_enemy(self):
        hero = Hero("Hero", 1, 50, 100)
        enemy = Hero("Enemy", 1, 50, 50)

        result = hero.battle(enemy)
        self.assertEqual(result, "Draw")

    def test_battle_enemy_hero_health_minus(self):
        hero = Hero("Hero", 1, 100, 100)
        enemy = Hero("Enemy", 1, 50, 50)
        result = hero.battle(enemy)
        self.assertEqual(hero.level, 2)
        self.assertEqual(hero.health, 55)
        self.assertEqual(hero.damage, 105)
        self.assertEqual(result, "You win")

    def test_battle_enemy_wins(self):
        hero = Hero("Hero", 1, 50, 50)
        enemy = Hero("Enemy", 1, 100, 100)
        result = hero.battle(enemy)
        self.assertEqual(enemy.level, 2)
        self.assertEqual(enemy.health, 55)
        self.assertEqual(enemy.damage, 105)
        self.assertEqual(result, "You lose")


if __name__ == "__main__":
    unittest.main()







