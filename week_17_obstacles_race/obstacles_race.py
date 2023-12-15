#
# Crea una función que evalúe si un/a atleta ha superado correctamente una
# carrera de obstáculos.
# - La función recibirá dos parámetros:
#      - Un array que sólo puede contener String con las palabras
#        "run" o "jump"
#      - Un String que represente la pista y sólo puede contener "_" (suelo)
#        o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#        será correcto y no variará el símbolo de esa parte de la pista.
#      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#      - Si hace "run" en "|" (valla), se variará la pista por "/".
# - La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#


from typing import List


def run_race(player: List[str], race: List[str]) -> bool:
    if len(player) != len(race):
        return False
    else:
        race_str = "".join(race)
        result = ""
        for i in range(0, len(player)):
            if player[i] == "run" and race[i] != "_":
                result += "x"
            elif player[i] == "jump" and race[i] != "|":
                result += "/"
            else:
                result += race[i]
        return race_str == result


my_player = ["run", "run", "jump", "run", "jump", "run"]
my_race = ["_", "_", "|", "_", "|", "_"]
print(run_race(my_player, my_race))