#
#  Enunciado: Crea una función que sea capaz de encriptar y desencriptar texto
#  utilizando el algoritmo de encriptación de Karaca
# (debes buscar información sobre él).
#

import re

karaca_encryption = {
    "a": 0,
    "e": 1,
    "i": 2,
    "o": 3,
    "u": 4,
}

karaca_decryption = {
    "0": "a",
    "1": "e",
    "2": "i",
    "3": "o",
    "4": "u",
}


def encrypt_word(word):
    result = ""
    for i in word:
        if i in karaca_encryption:
            result = str(karaca_encryption[i]) + result
        else:
            result = i + result
    return result + "aca"


def encrypt_text(text):
    text_arr = re.split(r"\s", text.lower())
    encryption = ""
    for word in text_arr:
        result = encrypt_word(word)
        encryption += result + " "
    return encryption[0:len(encryption) - 1]


def decrypt_word(word):
    current_word = "".join(reversed(word[0:len(word) - 3]))
    decrypted_word = ""
    for i in current_word:
        if i in karaca_decryption:
            decrypted_word += karaca_decryption[i]
        else:
            decrypted_word += i
    return decrypted_word


def decrypt_text(text):
    text_arr = re.split(r"\s", text.lower())
    decrypted_text = ""
    for i in text_arr:
        result = decrypt_word(i)
        decrypted_text += result + " "
    return decrypted_text[0:len(decrypted_text) - 1]


my_text = "hi my name is santiago"
my_text2 = "2haca ymaca 1m0naca s2aca 3g02tn0saca"
print(encrypt_text(my_text))
print(decrypt_text(my_text2))
