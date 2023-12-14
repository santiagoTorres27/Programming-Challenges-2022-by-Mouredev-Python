#
# Enunciado: Dado un array de números enteros positivos, donde cada uno
# representa unidades de bloques apilados, debemos calcular cuantas unidades
# de agua quedarán atrapadas entre ellos.
#
# - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
#
#        ⏹
#        ⏹
#  ⏹💧💧⏹
#  ⏹💧⏹⏹💧⏹
#  ⏹💧⏹⏹💧⏹
#  ⏹💧⏹⏹⏹⏹
#
#  Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
#   de agua. Suponemos que existe un suelo impermeable en la parte inferior
#  que retiene el agua.
#

def check_left_max(walls):
    max_walls = [walls[0]]
    for i in range(1, len(walls)):
        new_value = max(walls[i], max_walls[i - 1])
        max_walls.append(new_value)
    return max_walls


def check_right_max(walls):
    max_walls = [0] * len(walls)
    max_walls[len(walls) - 1] = walls[len(walls) - 1]
    for i in range(len(walls) - 2, -1, -1):
        new_value = max(walls[i], max_walls[i + 1])
        max_walls[i] = new_value
    return max_walls


def check_water_container(walls):
    left_walls = check_left_max(walls)
    right_walls = check_right_max(walls)
    container = []
    for i in range(len(walls)):
        min_value = min(left_walls[i], right_walls[i])
        new_value = min_value - walls[i]
        container.append(new_value)
    return sum(container)


my_walls = [4, 0, 3, 6, 1, 3]
print(check_water_container(my_walls))
