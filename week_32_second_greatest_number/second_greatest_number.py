#
# Dado un listado de números, encuentra el SEGUNDO más grande.
#

def find_second_greatest(numbers):
    numbers.sort(reverse=True)
    return numbers[1]


my_numbers = [-23, -45, 12, -44, -54, -100]
print(find_second_greatest(my_numbers))
