#
# Enunciado: Crea un programa se encargue de transformar un número binario
# a decimal sin utilizar funciones propias del lenguaje que
# lo hagan directamente.
#
import math


def binary_to_decimal(binary: str) -> int:
    binary_list = list(binary)
    binary_list.reverse()
    binary_list_int = [int(x) for x in binary_list]
    decimal = 0
    for i in range(len(binary_list_int)):
        operation = int(math.pow(2, i)) * binary_list_int[i]
        decimal += operation
    return decimal


print(binary_to_decimal("101011010111010101"))
