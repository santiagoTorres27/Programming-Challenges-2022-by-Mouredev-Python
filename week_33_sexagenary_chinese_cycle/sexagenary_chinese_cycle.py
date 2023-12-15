#
# Enunciado: Crea un función, que dado un año, indique el elemento
# y animal correspondiente en el ciclo sexagenario del zodíaco chino.
# - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
# - El ciclo sexagenario se corresponde con la combinación de los elementos
#  madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
#  conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
#  (en este orden).
# - Cada elemento se repite dos años seguidos.
# - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
#
elements = ["wood", "wood", "fire", "fire", "earth", "earth", "metal", "metal", "water", "water"]
animals = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep", "monkey", "rooster", "dog", "pig"]


def check_base_year(year):
    if year < 1984:
        while year < 1984:
            year = year + 60
    helper = year - 1984
    if helper < 60:
        return helper
    else:
        while helper > 60:
            helper = helper - 60
        if helper == 60:
            return 0
        return helper


def chinese_year(year):
    full_elements = elements * 6
    full_animals = animals * 5
    index = check_base_year(year)
    element = full_elements[index]
    animal = full_animals[index]
    print(f"{year} -> {element} - {animal}")


chinese_year(1900)
