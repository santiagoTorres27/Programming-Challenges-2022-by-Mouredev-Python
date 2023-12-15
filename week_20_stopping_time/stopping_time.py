#
# Crea una función que sume 2 números y retorne su resultado pasados
# unos segundos.
# - Recibirá por parámetros los 2 números a sumar y los segundos que
#   debe tardar en finalizar su ejecución.
# - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#   asíncrona, es decir, sin detener la ejecución del programa principal.
#   Se podría ejecutar varias veces al mismo tiempo.
#
import threading
import time


def add_numbers(num1, num2):
    return num1 + num2


def start_timer(num1: int, num2: int, seconds: int):
    time.sleep(seconds)
    result = add_numbers(num1, num2)
    print(result)


start_timer(10, 20, 2)
