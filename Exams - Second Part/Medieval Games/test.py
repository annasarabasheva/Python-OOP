from movie_app.controller import Controller
from movie_app.player import Player
from movie_app.supply.drink import Drink
from movie_app.supply.food import Food
from movie_app.controller import Controller
from movie_app.player import Player
from movie_app.supply.drink import Drink
from movie_app.supply.food import Food

# controller = Controller()
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# #print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.add_supply(cheese))
# print(controller.add_player(first_player, second_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
# print(controller)

controller = Controller()
first_player = Player('Peter', 15)
second_player = Player('Peter', 15)
print(controller.add_player(first_player, second_player))