#
# Escribe una función que calcule y retorne el factorial de un número dado
# de forma recursiva.
#

def recursive_factorial(num: int):
    if num <= 2:
        return num
    else:
        return recursive_factorial(num - 1) * num


print(recursive_factorial(5))
