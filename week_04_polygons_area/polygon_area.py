#
# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.
#

from classes import Triangle, Square, Rectangle


def get_triangle_area():
    try:
        base = int(input("base: "))
        height = int(input("height: "))
        t1 = Triangle(base, height)
        print(f"Area: {t1.get_area()}")
    except ValueError:
        print("Letters are not allowed")


def get_square_area():
    try:
        side = int(input("side: "))
        s1 = Square(side)
        print(f"Area: {s1.get_area()}")
    except ValueError:
        print("Letters are not allowed")


def get_rectangle_area():
    try:
        base = int(input("base: "))
        height = int(input("height: "))
        r1 = Rectangle(base, height)
        print(f"Area: {r1.get_area()}")
    except ValueError:
        print("Letters are not allowed")


while True:
    print("1. Triangle\n2. Square\n3. Rectangle")
    option = input("Select the figure: ")
    if option == "1":
        get_triangle_area()
    elif option == "2":
        get_square_area()
    elif option == "3":
        get_rectangle_area()
    else:
        print("Option not allowed")

    response = input("Do you want to continue? Y/n")
    if not response.lower() == "y":
        break
