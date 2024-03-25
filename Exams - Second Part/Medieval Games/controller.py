from movie_app.player import Player
from movie_app.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args: Player):
        names = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                names.append(player.name)
        return f"Successfully added: {', '.join(names)}"

    def add_supply(self, *args: Supply):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type in ["Food", "Drink"]:
            self.supplies.reverse()
            for supply in self.supplies.copy():  # [::-1].copy():
                if supply.__class__.__name__ == sustenance_type:
                    for player in self.players:
                        if player.name == player_name:
                            if player.stamina == 100:
                                self.supplies.reverse()
                                return f"{player_name} have enough stamina."
                            if player.stamina + supply.energy > 100:
                                player.stamina = 100
                            else:
                                player.stamina += supply.energy
                            supply_name = supply.name

                            self.supplies.remove(supply)
                            self.supplies.reverse()
                            return f"{player_name} sustained successfully with {supply_name}."
                    return

            self.supplies.reverse()
            if sustenance_type == "Food":
                raise Exception("There are no food supplies left!")
            elif sustenance_type == "Drink":
                raise Exception("There are no drink supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):
        stamina_first = 0
        stamina_second = 0
        for player in self.players:
            if player.name == first_player_name:
                stamina_first += player.stamina
            elif player.name == second_player_name:
                stamina_second += player.stamina
        if stamina_first == 0 and stamina_second == 0:
            return f"Player {first_player_name} does not have enough stamina.\nPlayer {second_player_name} does not have enough stamina."
        elif stamina_first == 0 and stamina_second > 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif stamina_first > 0 and stamina_second == 0:
            return f"Player {second_player_name} does not have enough stamina."
        if stamina_first > 0 and stamina_second > 0:
            if stamina_first < stamina_second:
                for player in self.players:
                    if player.name == second_player_name:
                        if player.stamina - (1 / 2 * stamina_first) <= 0:
                            player.stamina = 0
                            return f"Winner: {first_player_name}"
                        else:
                            player.stamina -= (1 / 2 * stamina_first)
                            stamina_second = player.stamina

                for player in self.players:
                    if player.name == first_player_name:
                        if player.stamina - (1 / 2 * stamina_second) <= 0:
                            player.stamina = 0
                            return f"Winner: {second_player_name}"
                        player.stamina -= (1 / 2 * stamina_second)
                        stamina_first = player.stamina

            elif stamina_second < stamina_first:
                for player in self.players:
                    if player.name == first_player_name:
                        if player.stamina - (1 / 2 * stamina_second) <= 0:
                            player.stamina = 0
                            return f"Winner: {second_player_name}"
                        player.stamina -= (1 / 2 * stamina_second)
                        stamina_first = player.stamina

                for player in self.players:
                    if player.name == second_player_name:
                        if player.stamina - (1 / 2 * stamina_first) <= 0:
                            player.stamina = 0
                            return f"Winner: {first_player_name}"
                        player.stamina -= (1 / 2 * stamina_first)
                        stamina_second = player.stamina

            if stamina_first > stamina_second:
                return f"Winner: {first_player_name}"
            else:
                return f"Winner: {second_player_name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

        self.sustain_all_players()

    def sustain_all_players(self):
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += f"{str(player)}\n"
        # self.supplies = self.supplies[::-1]
        for supply in self.supplies:
            result += f"{supply.details()}\n"

        return result
