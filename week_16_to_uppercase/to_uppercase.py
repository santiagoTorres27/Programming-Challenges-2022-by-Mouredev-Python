#
# Crea una función que reciba un String de cualquier tipo y se encargue de
# poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que
# lo resuelvan directamente.
#

import re


def text_to_uppercase(text: str) -> str:
    words = re.split(r"\s+", text)
    result = ""
    for i in words:
        current_word = i[0].upper() + i[1:]
        result = result + current_word + " "
    return result[0:len(result) - 1]


my_text = "Hello everybody, how are you today?"
print(text_to_uppercase(my_text))
