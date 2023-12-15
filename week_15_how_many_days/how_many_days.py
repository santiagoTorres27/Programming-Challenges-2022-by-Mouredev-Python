#
# Crea una función que calcule y retorne cuántos días hay entre dos cadenas
# de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se
#  lanzará una excepción.
#

from datetime import datetime


def calculate_days(date1: str, date2: str):
    if date1 > date2:
        aux = date1
        date1 = date2
        date2 = aux
    start_date = datetime.strptime(date1, "%d/%m/%Y")
    finish_date = datetime.strptime(date2, "%d/%m/%Y")
    total_days = start_date - finish_date
    return f"{total_days.days} days have passed"


date_1 = "29/12/1992"
date_2 = "12/12/2023"
print(calculate_days(date_1, date_2))
