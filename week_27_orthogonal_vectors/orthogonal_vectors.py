#
# Crea un programa que determine si dos vectores son ortogonales.
# - Los dos array deben tener la misma longitud.
# - Cada vector se podría representar como un array. Ejemplo: [1, -2]
#

def are_orthogonal_vectors(vector1, vector2):
    result = (vector1[0] * vector1[1]) + (vector2[0] * vector2[1])
    return result == 0


my_vector1 = [4, 2]
my_vector2 = [-1, 8]
print(are_orthogonal_vectors(my_vector1, my_vector2))
