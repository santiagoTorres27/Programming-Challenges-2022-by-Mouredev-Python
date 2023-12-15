#
# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
#  la que el siguiente siempre es la suma de los dos anteriores.
#  0, 1, 1, 2, 3, 5, 8, 13...
#

def print_fibonacci_sequence(length: int):
    fibonacci_arr = [0, 1]
    for i in range(2, length + 1):
        new_number = fibonacci_arr[len(fibonacci_arr) - 1] + fibonacci_arr[len(fibonacci_arr) - 2]
        fibonacci_arr.append(new_number)
    for i in fibonacci_arr:
        print(i)


print_fibonacci_sequence(50)
