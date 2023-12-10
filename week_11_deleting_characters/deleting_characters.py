#
# Crea una función que reciba dos cadenas como parámetro (str1, str2)
# e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO
#   estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  estén presentes en str1.
#

def delete_characters(str1, str2):
    result = ""
    for i in str1:
        if i not in str2:
            result += i
    return result


def execute_deleting_characters(str1: str, str2: str):
    out1 = delete_characters(str1, str2)
    out2 = delete_characters(str2, str1)
    print(out1)
    print(out2)


execute_deleting_characters("hola", "adios")
