#
# Crea un programa que sea capaz de transformar texto natural a código
# morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar
#   la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#   o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en
#   https://es.wikipedia.org/wiki/Código_morse.
#
import re
from morse import text_to_morse_dict, morse_to_text_dict


def word_to_text(word):
    letters = word.split(" ")
    translation = ""
    for i in letters:
        if morse_to_text_dict.get(i):
            translation += morse_to_text_dict.get(i)
    return translation


def translate_to_natural_text(text):
    text_words = text.split("  ")
    translation = ""
    for i in text_words:
        translation += word_to_text(i) + " "
    return translation


def word_to_morse(word) -> str:
    translation = ""
    for i in word.upper():
        if text_to_morse_dict.get(i):
            translation += text_to_morse_dict.get(i) + " "
    return translation


def translate_to_morse(text):
    words = re.split(r"\s+", text)
    morse_translation = ""
    for i in words:
        morse_translation += word_to_morse(i) + " "
    return morse_translation


def translate_text(text: str):
    patron = re.compile('^[\\s.-]*$')
    is_morse = bool(patron.search(text))
    if is_morse:
        print(translate_to_natural_text(text))
    else:
        print(translate_to_morse(text))


my_text = "hola a    todos"
my_text_2 = ".... --- .-.. .-  .-  - --- -.. --- ..."
translate_text(my_text_2)
