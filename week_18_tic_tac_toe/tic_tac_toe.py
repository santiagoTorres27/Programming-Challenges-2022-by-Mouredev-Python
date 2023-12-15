#
# Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
# y retorne lo siguiente:
# - "X" si han ganado las "X"
# - "O" si han ganado los "O"
# - "Empate" si ha habido un empate
# - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
#   O si han ganado los 2.
# Nota: La matriz puede no estar totalmente cubierta.
# Se podría representar con un vacío "", por ejemplo.
#

win_results = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 4],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def check_result(game) -> str:
    for i in win_results:
        line = set()
        for j in i:
            line.add(game[j])
        if len(line) == 1:
            winner = line.pop()
            return winner
    return "tie"


def play_game(game):
    arr = []
    for i in game:
        for j in i:
            arr.append(j)
    return check_result(arr)


my_game = [
    ["x", "o", "x"],
    ["o", "x", "o"],
    ["x", " ", " "]
]

print("Winner is: " + play_game(my_game))
