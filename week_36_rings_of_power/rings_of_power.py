#
# Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales
# a Sauron contra otras bondadosas que no quieren que el mal reine
# sobre sus tierras.
# Cada raza tiene asociado un "valor" entre 1 y 5:
# - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
#   Númenóreanos (4), Elfos (5)
# - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
#   Huargos (3), Trolls (5)
# Crea un programa que calcule el resultado de la batalla entre
# los 2 tipos de ejércitos:
# - El resultado puede ser que gane el bien, el mal, o exista un empate.
#   Dependiendo de la suma del valor del ejército y el número de integrantes.
# - Cada ejército puede estar compuesto por un número de integrantes variable
#   de cada raza.
# - Tienes total libertad para modelar los datos del ejercicio.
# Ej: 1 Peloso pierde contra 1 Orco
#     2 Pelosos empatan contra 1 Orco
#     3 Pelosos ganan a 1 Orco
#

from enum import Enum
import random


class KindRaces(Enum):
    PELOSO = 1
    SURENO_BUENO = 2
    ENANO = 3
    NUMENOREANO = 4
    ELFO = 5


class EvilRaces(Enum):
    SURENO_MALO = 2
    ORCO = 2
    GOBLIN = 2
    HUARGO = 3
    TROLL = 5


def generate_army(length, kind=True):
    kind_army = list(KindRaces)
    evil_army = list(EvilRaces)
    army = []
    for _ in range(length):
        if kind:
            random_index = random.randint(1, len(kind_army) - 1)
            army.append(kind_army[random_index])
        else:
            random_index = random.randint(1, len(evil_army) - 1)
            army.append(evil_army[random_index])
    return army


def init_battle():
    kind_army = generate_army(5)
    evil_army = generate_army(5, False)

    kind_army_force = sum([x.value for x in kind_army])
    evil_army_force = sum([x.value for x in evil_army])

    print("KIND ARMY ================================")
    for i in kind_army:
        print(i.name)
    print(f"FORCE: {kind_army_force}")

    print("\nEVIL ARMY ==============================")
    for i in evil_army:
        print(i.name)
    print(f"FORCE: {evil_army_force}")

    if kind_army_force == evil_army_force:
        print("\nTIED BATTLE!")
    elif kind_army_force > evil_army_force:
        print("\nKIND ARMY WINS!!")
    elif kind_army_force < evil_army_force:
        print("\nEVIL ARMY WINS :(")


init_battle()
