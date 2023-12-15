#
# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
#    las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.
#

def sort_word(word):
    arr = list(word.lower())
    arr.sort()
    return "".join(arr)


def is_anagram(word1: str, word2: str) -> bool:
    if word1.lower() == word2.lower():
        return False
    else:
        word1_sorted = sort_word(word1)
        word2_sorted = sort_word(word2)
        return word1_sorted == word2_sorted


print(is_anagram("listen", "SILENT"))
