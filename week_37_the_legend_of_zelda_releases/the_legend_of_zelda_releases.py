#
#  Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"!
#  Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
# Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
#  "The Legend of Zelda" de la historia?
#  Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
#  que tú selecciones.
# - Debes buscar cada uno de los títulos y su día de lanzamiento
#   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
#

from datetime import datetime
import json


class ZeldaGame:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f"{self.name}: {self.date}"


def generate_zelda_games_list():
    zelda_gamelist = {}
    file_path = "/mnt/nvme0n1p4/Projects/PycharmProjects/Programming-Challenges-2022-by-Mouredev-Python/week_37_the_legend_of_zelda_releases/zelda.json"

    with open(file_path, "r") as json_file:
        zelda_games = json.load(json_file)

    zelda_game_releases = zelda_games["zelda_game_launches"]
    for i in range(len(zelda_game_releases)):
        game_name = zelda_game_releases[i]["name"]
        game_release = zelda_game_releases[i]["date"]
        date = datetime.strptime(game_release, "%Y-%m-%d").date()
        zelda_gamelist[i] = ZeldaGame(game_name, date)
    return zelda_gamelist


def check_time():
    games = generate_zelda_games_list()
    for key, game in games.items():
        print(f"{key} | {game}")

    try:
        first_game_index = int(input("Select first game index: "))
        second_game_index = int(input("Select second game index: "))

        if first_game_index in games and second_game_index in games:
            game1 = games.get(first_game_index)
            game2 = games.get(second_game_index)
            days_difference = abs((game1.date - game2.date).days)

            print(f"\nBetween '{game1.name}' \n&\n'{game2.name}' \n{days_difference} days have passed!")
        else:
            print("The index provided is not in the list")

    except ValueError:
        print("You cannot enter letters...")


def init():
    while True:
        check_time()
        option = input("\nDo you want to start again? Y/n")
        if option.upper() != "Y":
            return


init()
