#
# Simula el funcionamiento de una máquina expendedora creando una operación
# que reciba dinero (array de monedas) y un número que indique la selección
# del producto.
# - El programa retornará el nombre del producto y un array con el dinero
#   de vuelta (con el menor número de monedas).
# - Si el dinero es insuficiente o el número de producto no existe,
#  deberá indicarse con un mensaje y retornar todas las monedas.
# - Si no hay dinero de vuelta, el array se retornará vacío.
# - Para que resulte más simple, trabajaremos en céntimos con monedas
#  de 5, 10, 50, 100 y 200.
# - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
#

from classes import Product
import re

product_list = {
    1: Product("product 1", 300),
    2: Product("product 2", 150),
    3: Product("product 3", 450),
    4: Product("product 4", 630),
}


def make_payment(money, product_price):
    change = money - product_price
    change_aux = change
    coins_200 = 0
    coins_100 = 0
    coins_50 = 0
    coins_10 = 0
    coins_5 = 0

    while change != 0:
        if change - 200 >= 0:
            coins_200 = coins_200 + 1
            change -= 200
        elif change - 100 >= 0:
            coins_100 = coins_100 + 1
            change -= 100
        elif change - 50 >= 0:
            coins_50 = coins_50 + 1
            change -= 50
        elif change - 10 >= 0:
            coins_10 = coins_10 + 1
            change -= 10
        elif change - 5 >= 0:
            coins_5 = coins_5 + 1
            change -= 5

    print(f"200: {coins_200}")
    print(f"100: {coins_100}")
    print(f"50: {coins_50}")
    print(f"10: {coins_10}")
    print(f"5: {coins_5}")
    return change_aux


def print_options_available():
    print()
    for key, product in product_list.items():
        print(f"{key}: {product}")
    option = int(input("Please enter the product key: "))
    if product_list.get(option):
        return option
    else:
        return None


def insert_money() -> int:
    print("Please insert money, each coin must be followed by an empty space")
    print("Coins allowed: 200, 100, 50, 10, 5")
    coins = input()
    coins_arr = re.split("\\s+", coins)
    try:
        total_coins = [int(x) for x in coins_arr]
        valid_coins = {5, 10, 50, 100, 200}
        if all(i in valid_coins for i in total_coins):
            total_money = sum(total_coins)
            return total_money
        else:
            print("You didn't enter valid value coins, please try it again")
            return 0
    except ValueError:
        print("You cannot enter letters, please try it again")


def init_vending_machine():
    while True:
        option = print_options_available()
        if option is None:
            print("The product selected doesn't exist")
        else:
            product = product_list.get(option)
            product_price = product.price
            total_money = insert_money()
            if total_money < product_price:
                print("Insufficient funds. Please insert the correct amount to purchase this item.")
            elif total_money != 0:
                print("\nThanks for purchasing!")
                print(f"Purchased item: {product}")
                change = make_payment(total_money, product_price)
                print(f"Please take your change: {change}")

        want_continue = input("\nDo you want to shop again? Y/n ")
        if want_continue.upper() != "Y":
            return


init_vending_machine()
