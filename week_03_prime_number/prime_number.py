#
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
#

def is_prime_number(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def print_prime_numbers(length: int):
    for i in range(length):
        if is_prime_number(i):
            print(i)


print_prime_numbers(100)
