#
# Escribe una función que reciba un texto y retorne verdadero o
# falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee
# de izquierda a derecha que de derecha a izquierda.
#  NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.
#

import re


def is_palindrome(text: str):
    words = re.findall(r"\w+", text.lower())
    cleaned_text = "".join(words)
    for i in range(0, len(cleaned_text) // 2):
        if cleaned_text[i] != cleaned_text[len(cleaned_text) - 1 - i]:
            return False
    return True


print(is_palindrome("Ana lleva, al oso la avellana."))
