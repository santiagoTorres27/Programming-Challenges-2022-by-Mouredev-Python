#
# Enunciado: Crea un función que reciba un texto y retorne la vocal que
#  más veces se repita.
#  - Ten cuidado con algunos casos especiales.
#  - Si no hay vocales podrá devolver vacío.
#

import re


def most_common_vowel(text):
    pattern = re.compile(r"[aeiou]")
    results = pattern.findall(text.lower())
    occurrences = {}
    most_repeated_vowel = ""
    most_repeated_vowel_occurrences = 0
    for vowel in results:
        if vowel not in occurrences:
            occurrences[vowel] = 1
        else:
            occurrences[vowel] = occurrences[vowel] + 1
    for key, value in occurrences.items():
        if value > most_repeated_vowel_occurrences:
            most_repeated_vowel_occurrences = value
            most_repeated_vowel = key
    return f"Vowel: {most_repeated_vowel} -> {most_repeated_vowel_occurrences}"


my_text = "hola a todos aaaa dsd a"
print(most_common_vowel(my_text))
