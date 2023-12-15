#
# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#

def reversing_strings(text: str) -> str:
    reversed_text = ""
    for i in text:
        reversed_text = i + reversed_text
    return reversed_text


print(reversing_strings("Hola mundo"))
