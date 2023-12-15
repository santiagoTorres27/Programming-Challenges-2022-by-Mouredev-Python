#
# Enunciado: Crea una función que calcule el valor del parámetro perdido
# correspondiente a la ley de Ohm.
# - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
#   el valor del tercero (redondeado a 2 decimales).
# - Si los parámetros son incorrectos o insuficientes, la función retornará
#   la cadena de texto "Invalid values".
#

def calculate_lost_value(v=0, r=0, i=0):
    result = {}
    if v == 0:
        v = i * r
        result["v"] = v
    elif r == 0:
        r = v / i
        result["r"] = r
    elif i == 0:
        i = v / r
        result["i"] = i
    return result


lost_value = calculate_lost_value(v=2, i=34)
print(lost_value)
