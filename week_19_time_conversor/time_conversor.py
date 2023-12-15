#
# Crea una función que reciba días, horas, minutos y segundos (como enteros)
# y retorne su resultado en milisegundos.
#

def time_to_millis(days: int, hours: int, minutes: int, seconds: int):
    days_to_millis = 86400 * days * 1000
    hours_to_millis = 3600 * hours * 1000
    minutes_to_millis = 60 * minutes * 1000
    seconds_to_millis = seconds * 1000
    return days_to_millis + hours_to_millis + minutes_to_millis + seconds_to_millis


print(time_to_millis(1, 1, 1, 1))
