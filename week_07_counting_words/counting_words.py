#
# Crea un programa que cuente cuantas veces se repite cada palabra
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que
#  lo resuelvan automáticamente.
#

import re


def count_words(text: str):
    arr = re.findall(r"\w+", text.lower())
    occurrences = {}
    for i in arr:
        if not occurrences.get(i):
            occurrences[i] = 1
        else:
            occurrences[i] = occurrences.get(i) + 1
    for key, value in occurrences.items():
        print(f"{key} -> {value}")


my_text = "Hola a todos, hola,    a hola, hola, todos..."
count_words(my_text)
