#
# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "R" (piedra), "P" (papel)
#   o "S" (tijera).
# - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
#


def check_play(game):
    player1 = game[0]
    player2 = game[1]
    if player1 == player2:
        return "tie"
    elif (player1 == "R" and player2 == "S") or (player1 == "P" and player2 == "R") or (
            player1 == "S" and player2 == "P"):
        return "player 1"
    elif (player1 == "S" and player2 == "R") or (player1 == "R" and player2 == "P") or (
            player1 == "P" and player2 == "S"):
        return "player 2"


def play_game(game_list):
    player1_wins = 0
    player2_wins = 0
    for i in game_list:
        result = check_play(i)
        if result == "player 1":
            player1_wins = player1_wins + 1
        else:
            player2_wins = player2_wins + 1
    if player1_wins == player2_wins:
        return "Tie game"
    elif player1_wins > player2_wins:
        return "Player 1 wins"
    elif player2_wins > player1_wins:
        return "Player 2 wins"


my_game = [("R", "S"), ("S", "R"), ("P", "S")]

print(play_game(my_game))
