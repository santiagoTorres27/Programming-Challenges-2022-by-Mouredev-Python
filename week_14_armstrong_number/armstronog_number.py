#
# Escribe una función que calcule si un número dado es un número de Armstrong
# (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información
# al respecto.
#
import math


def get_digits(number):
    digits = []
    while number > 0:
        res = number % 10
        digits.append(res)
        number = number // 10
    return digits


def is_armstrong_number(number: int):
    digits = get_digits(number)
    number_length = len(str(number))
    result = 0
    for i in digits:
        operation = math.pow(i, number_length)
        result = result + operation
    return result == number


print(is_armstrong_number(1634))
print(is_armstrong_number(54748))
print(is_armstrong_number(4355))
