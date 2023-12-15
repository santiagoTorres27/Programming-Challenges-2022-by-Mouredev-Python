#
# Enunciado: Crea una función que transforme grados Celsius en Fahrenheit
# y viceversa.
#
# - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
#   y su unidad ("C" o "F").
# - En caso contrario retornará un error.
# - ¿Quieres emplear lo aprendido en este reto?
#   Revisa el reto mensual y crea una App:
#   https://retosdeprogramacion.com/mensuales2022
#

import re


def convert_to_fahrenheit(celsius):
    return celsius * (9 / 5) + 32


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_temperature(temperature):
    temperature = temperature.replace(" ", "").upper()
    if temperature[len(temperature) - 1] == "º" and (
            temperature[len(temperature) - 2] == "F" or temperature[len(temperature) - 2] == "C"):
        unit = temperature[len(temperature) - 2]

        try:
            value_str = temperature[0:len(temperature) - 2]
            value = int(value_str)
            if unit == "C":
                result = str(convert_to_fahrenheit(value)) + "Fº"
            else:
                result = str(convert_to_celsius(value)) + "Cº"
            return result
        except ValueError:
            print("Incorrect temperature value")
    else:
        print("Invalid")


my_temperature = "   4 534 f   º      "
print(convert_temperature(my_temperature))
