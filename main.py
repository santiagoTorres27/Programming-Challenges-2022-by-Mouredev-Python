#
# Crea una función que imprima los 30 próximos años bisiestos
# siguientes a uno dado.
# - Utiliza el menor número de líneas para resolver el ejercicio.
#

def is_leap_year(year: int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False


def find_next_leap_year(current_year):
    if is_leap_year(current_year):
        return current_year
    else:
        while not is_leap_year(current_year):
            current_year = current_year + 1
    return current_year


def print_30_next_leap_years(current_year):
    next_year = find_next_leap_year(current_year)
    for _ in range(30):
        print(next_year)
        next_year = next_year + 4


print_30_next_leap_years(2025)
