#
# Enunciado: Dado un array de enteros ordenado y sin repetidos,
# crea una función que calcule y retorne todos los que faltan entre
# el mayor y el menor.
# - Lanza un error si el array de entrada no es correcto.
#

def check_greatest(numbers):
    greatest = numbers[0]
    for i in numbers:
        if i > greatest:
            greatest = i
    return greatest


def check_lowest(numbers):
    lowest = numbers[0]
    for i in numbers:
        if i < lowest:
            lowest = i
    return lowest


def lost_numbers(numbers):
    greatest = check_greatest(numbers)
    lowest = check_lowest(numbers)
    lost_numbers_arr = []
    for i in range(lowest, greatest + 1):
        if i not in numbers:
            lost_numbers_arr.append(i)
    print(lost_numbers_arr)


my_numbers = [1, 2, 7, 8, 9]
lost_numbers(my_numbers)
