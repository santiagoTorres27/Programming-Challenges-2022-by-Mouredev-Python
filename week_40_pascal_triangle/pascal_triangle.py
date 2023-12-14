#
# Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
# indicándole únicamente el tamaño del lado.
#
# - Aquí puedes ver rápidamente cómo se calcula el triángulo:
#  https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
#

def generate_next_line(last_line):
    arr = []
    for i in range(len(last_line) - 1):
        new_number = last_line[i] + last_line[i + 1]
        arr.append(new_number)
    arr.insert(0, 1)
    arr.append(1)
    return arr


def generate_pascal_triangle(length: int):
    triangle = [[1], [1, 1]]
    if length > 2:
        for i in range(2, length):
            last_line = triangle[len(triangle) - 1]
            next_line = generate_next_line(last_line)
            triangle.append(next_line)
        return triangle
    elif length == 2:
        return triangle
    elif length == 1:
        return triangle[0]
    else:
        return None


def print_pascal_triangle(length: int):
    triangle = generate_pascal_triangle(length)
    if triangle is None:
        print("No triangle generated")
    else:
        for i in triangle:
            print(i)


print_pascal_triangle(5)
