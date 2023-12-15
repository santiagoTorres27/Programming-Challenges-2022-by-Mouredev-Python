#
# Enunciado: Crea una función que retorne el número total de bumeranes de
# un array de números enteros e imprima cada uno de ellos.
# - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
#  seguidos, en el que el primero y el último son iguales, y el segundo
#  es diferente. Por ejemplo [2, 1, 2].
# - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2]
#  y [4, 2, 4]).
#

def check_boomerang(arr):
    if len(arr) == 3 and arr[0] == arr[2]:
        return True
    return False


def get_boomerangs(numbers):
    arr = []
    for i in range(len(numbers) - 2):
        new_arr = []
        for j in range(i, i + 3):
            new_arr.append(numbers[j])
        if check_boomerang(new_arr):
            arr.append(new_arr)
    return arr


my_numbers = [2, 1, 2, 3, 3, 4, 2, 4]
print(get_boomerangs(my_numbers))
