#
# Enunciado: Crea un programa que calcule el daño de un ataque durante
# una batalla Pokémon.
# - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
# - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
# - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico
#  (buscar su efectividad)
# - El programa recibe los siguientes parámetros:
# - Tipo del Pokémon atacante.
# - Tipo del Pokémon defensor.
# - Ataque: Entre 1 y 100.
# - Defensa: Entre 1 y 100.
#

from classes import Kind, Pokemon
from messages import tied_msg, win_msg, lose_msg
import random

pokemon_list = {
    1: Pokemon("Charizard", 84, 74, Kind.FIRE),
    2: Pokemon("Vaporeon", 65, 60, Kind.WATER),
    3: Pokemon("Gengar", 65, 60, Kind.PLANT),
    4: Pokemon("Jolteon", 70, 65, Kind.ELECTRIC),
}


def select_pokemon():
    for key, value in pokemon_list.items():
        print(f"{key}: {value}")
    try:
        pokemon_selected = int(input("Select your pokemon: "))
        if pokemon_selected not in pokemon_list:
            return 0
        return pokemon_selected
    except ValueError:
        print("Letters are not allowed")


def generate_rival(my_pokemon_index):
    while True:
        result = random.randint(1, len(pokemon_list))
        if result != my_pokemon_index:
            return result


def init_battle(my_pokemon_index, rival_pokemon_index):
    my_pokemon = pokemon_list.get(my_pokemon_index)
    my_rival = pokemon_list.get(rival_pokemon_index)

    print("\n‍🔥️ 🔥 🔥 🔥 🔥 🔥 🔥 🔥 🔥 F I G H T 🔥 🔥 🔥 🔥 🔥 🔥 🔥 🔥 🔥")
    print(f"Me: {my_pokemon}")
    print(f"Rival: {my_rival}")

    print("\n⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ S T A R T I N G  B A T T L E ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️️")

    while my_pokemon.life > 0 and my_rival.life > 0:
        my_pokemon_damage = my_pokemon.hit()
        my_rival_damage = my_rival.hit()

        my_pokemon.receive_damage(my_rival_damage)
        my_rival.receive_damage(my_pokemon_damage)

        print(f"♥️ {my_pokemon.name} (Me): {my_pokemon.life}")
        print(f"💥️ {my_rival.name} (Rival): {my_rival.life}")

        if my_pokemon.life == 0 and my_rival.life == 0:
            print(tied_msg)
        elif my_pokemon.life <= 0:
            print(lose_msg)
        elif my_rival.life <= 0:
            print(win_msg)

        input("\nPress any key to continue...")


def init_game():
    while True:
        my_pokemon = select_pokemon()
        rival_pokemon = generate_rival(my_pokemon)
        init_battle(my_pokemon, rival_pokemon)
        option = input("\nDo you want to play again? Y/n")
        if option.upper() != "Y":
            return


init_game()
