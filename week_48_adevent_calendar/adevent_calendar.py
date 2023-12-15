#
# ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
# 24 días, 24 regalos sorpresa relacionados con desarrollo de software,
# ciencia y tecnología desde el 1 de diciembre.
#
# Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
# lo siguiente:
# - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
#   de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
# - Si la fecha es anterior: Cuánto queda para que comience el calendario.
# - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
#
# Notas:
# - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
#   y finaliza a las 23:59:59.
# - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
#   y segundos.
# - 🎁 Cada persona que aporte su solución entrará en un nuevo sorteo
#  del calendario de aDEViento hasta el día de su corrección
#   (sorteo exclusivo para quien entregue su solución).
#

from datetime import datetime

adevent_calendar = {
    "2022-12-01": "Gift 1",
    "2022-12-02": "Gift 2",
    "2022-12-03": "Gift 3",
    "2022-12-04": "Gift 4",
    "2022-12-05": "Gift 5",
    "2022-12-06": "Gift 6",
    "2022-12-07": "Gift 7",
    "2022-12-08": "Gift 8",
    "2022-12-09": "Gift 9",
    "2022-12-10": "Gift 10",
    "2022-12-11": "Gift 11",
    "2022-12-12": "Gift 12",
    "2022-12-13": "Gift 13",
    "2022-12-14": "Gift 14",
    "2022-12-15": "Gift 15",
    "2022-12-16": "Gift 16",
    "2022-12-17": "Gift 17",
    "2022-12-18": "Gift 18",
    "2022-12-19": "Gift 19",
    "2022-12-20": "Gift 20",
    "2022-12-21": "Gift 21",
    "2022-12-22": "Gift 22",
    "2022-12-23": "Gift 23",
    "2022-12-24": "Gift 24",
}


def get_difference_days(init_date, finish_date):
    days_difference = init_date - finish_date
    days = days_difference.days
    return days


def check_calendar(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    start_date = datetime(2022, 12, 1)
    finish_date = datetime(2022, 12, 24)
    if date > finish_date:
        days_difference = get_difference_days(date, finish_date)
        print(f"This date is {days_difference} days after aDEVent calendar 2022")
    elif date < start_date:
        days_difference = get_difference_days(date, start_date)
        print(f"This date is {days_difference} days before aDEVent calendar 2022")
    else:
        gift = adevent_calendar[date_str]
        print(f"Your gift for: {date_str} is {gift}")


my_date = "2023-12-01"
check_calendar(my_date)
