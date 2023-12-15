#
# Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
# - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
# - EXTRA: ¿Eres capaz de dibujar más figuras?
#

def print_square(length):
    for _ in range(length):
        for _ in range(length):
            print("*", end=" ")
        print()


def print_triangle(length):
    for i in range(length):
        for k in range(length - i, 0, -1):
            print(" ", end="")

        for j in range(i + 1):
            print("*", end=" ")
        print()


print_square(5)
print_triangle(6)
