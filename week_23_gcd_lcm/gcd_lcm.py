#
# Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
# que calcule el mínimo común múltiplo (mcm) de dos números enteros.
# - No se pueden utilizar operaciones del lenguaje que
#  lo resuelvan directamente.
#
import math


def find_divisors(num: int):
    divisor = 2
    divisors = []
    divisors_dict = {}
    while num > 1:
        if num % divisor == 0:
            divisors.append(divisor)
            num = num // divisor
        else:
            divisor = divisor + 1
    for i in divisors:
        if not divisors_dict.get(i):
            divisors_dict[i] = 1
        else:
            divisors_dict[i] = divisors_dict.get(i) + 1
    return divisors_dict


def least_common_multiple(num1, num2):
    divisors1 = find_divisors(num1)
    divisors2 = find_divisors(num2)
    result = {}
    result.update(divisors1)
    lcm = 1
    for key, value in divisors2.items():
        if key in result and result.get(key) < value:
            result[key] = value
        elif key not in result:
            result[key] = value
    for key, value in result.items():
        lcm *= math.pow(key, value)
    return lcm


def greatest_common_divisor(num1, num2):
    return (num1 * num2) / least_common_multiple(num1, num2)


number1 = 56
number2 = 35

lcm = least_common_multiple(number1, number2)
gcm = greatest_common_divisor(number1, number2)

print(f"Least common multiple: {lcm}")
print(f"Greatest common divisor: {gcm}")
