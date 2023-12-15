#
# Crea una función que ordene y retorne una matriz de números.
# - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
#  adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
#  o de mayor a menor.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
#  automáticamente.
#

from typing import List


def sort_list(numbers: List[int], asc=True):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(i):
            if asc:
                if numbers[j] > numbers[j + 1]:
                    temp = numbers[j]
                    numbers[j] = numbers[j + 1]
                    numbers[j + 1] = temp
            else:
                if numbers[j] < numbers[j + 1]:
                    temp = numbers[j]
                    numbers[j] = numbers[j + 1]
                    numbers[j + 1] = temp
    return numbers


my_list = [2, 4, 6, 4, 6, 22, 5, -56]
print(sort_list(my_list, False))
