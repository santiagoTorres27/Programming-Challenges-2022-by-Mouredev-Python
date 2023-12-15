#
# Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
# resultado e imprímelo.
# - El .txt se corresponde con las entradas de una calculadora.
# - Cada línea tendrá un número o una operación representada por un
#   símbolo (alternando ambos).
# - Soporta números enteros y decimales.
# - Soporta las operaciones suma "+", resta "-", multiplicación "*"
#   y división "/".
# - El resultado se muestra al finalizar la lectura de la última
#   línea (si el .txt es correcto).
# - Si el formato del .txt no es correcto, se indicará que no se han
#  podido resolver las operaciones.
#

def start_calculator():
    with open("calculator", "r") as file:
        items = [line.strip() for line in file.readlines()]
    last_operator = ""
    result = 0
    for i in items:
        if i == "+" or i == "-" or i == "/" or i == "*":
            last_operator = i
        else:
            number = int(i)
            if last_operator == "+":
                result += number
            elif last_operator == "-":
                result -= number
            elif last_operator == "*":
                result *= number
            elif last_operator == "/":
                result /= number
            else:
                result = number
    print(result)


start_calculator()
