#
# Crea un programa se encargue de transformar un número
#  decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#

def decimal_to_binary(number: int) -> str:
    binary = ""
    while number > 0:
        res = number % 2
        binary += str(res)
        number = number // 2
    return "".join(reversed(binary))


decimal_number = 456
print(decimal_to_binary(decimal_number))
