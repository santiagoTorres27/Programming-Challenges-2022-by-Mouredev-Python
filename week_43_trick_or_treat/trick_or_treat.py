#
# Enunciado: Este es un reto especial por Halloween.
# Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
# o Trato" y un listado (array) de personas con las siguientes propiedades:
# - Nombre de la niña o niño
# - Edad
# - Altura en centímetros
#
# Si las personas han pedido truco, el programa retornará sustos (aleatorios)
# siguiendo estos criterios:
# - Un susto por cada 2 letras del nombre por persona
# - Dos sustos por cada edad que sea un número par
# - Tres sustos por cada 100 cm de altura entre todas las personas
# - Sustos: 🎃 👻 💀 🕷 🕸 🦇
#
# Si las personas han pedido trato, el programa retornará dulces (aleatorios)
# siguiendo estos criterios:
# - Un dulce por cada letra de nombre
# - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
# - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
# - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
#

from classes import Kid
import random

kids = [
    Kid("Santiago", 8, 150),
    Kid("Clara", 12, 159),
    Kid("Juan", 9, 162),
    Kid("Sara", 11, 153),
]


def generate_scares():
    names_length = 0
    names_scares = 0
    age_scares = 0
    total_height = 0
    height_scares = 0
    for kid in kids:
        names_length += len(kid.name)
        total_height += kid.height
        if kid.age % 2 == 0:
            age_scares += 1
    names_scares = names_length // 2
    height_scares = total_height // 100
    return names_scares + age_scares + height_scares


def generate_items(num, kind):
    scares_list = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
    candies_list = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]
    result = []
    for i in range(num):
        if kind == "trick":
            random_index = random.randint(0, len(scares_list) - 1)
            result.append(scares_list[random_index])
        else:
            random_index = random.randint(0, len(candies_list) - 1)
            result.append(candies_list[random_index])
    return result


def print_list(arr):
    for i in arr:
        print(i)


def generate_candies():
    names_candies = 0
    age_candies = 0
    height_candies = 0
    for kid in kids:
        names_candies += len(kid.name)
        if kid.age <= 10:
            age_candies += kid.age // 3
        if kid.height <= 150:
            height_candies += kid.height // 50
    return names_candies + age_candies + height_candies


def generate_res(option):
    if option == 1:
        scares = generate_scares()
        trick = generate_items(scares, "trick")
        print_list(trick)
    elif option == 2:
        candies = generate_candies()
        treat = generate_items(candies, "treat")
        print_list(treat)
    else:
        print("Invalid option")


def init_program():
    while True:
        try:
            option = int(input("1 Trick or 2 Treat: "))
            generate_res(option)
        except ValueError:
            print("Letters are not allowed")

        response = input("\nDo you want to continue? Y/n")
        if response.upper() != "Y":
            return


init_program()
