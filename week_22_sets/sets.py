#
# Crea una función que reciba dos array, un booleano y retorne un array.
# - Si el booleano es verdadero buscará y retornará los elementos comunes
#   de los dos array.
# - Si el booleano es falso buscará y retornará los elementos no comunes
#   de los dos array.
# - No se pueden utilizar operaciones del lenguaje que
#   lo resuelvan directamente.
#

def join_sets(array1, array2, common_elements: bool):
    result = []
    if common_elements:
        for i in array1:
            if i in array2:
                result.append(i)
    else:
        for i in array1:
            if i not in array2:
                result.append(i)
        for j in array2:
            if j not in array1:
                result.append(j)
    return result


my_array1 = [1, 2, 3, 4]
my_array2 = [3, 4, 5, 6]
print(join_sets(my_array1, my_array2, False))
