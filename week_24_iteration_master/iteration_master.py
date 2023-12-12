#
# Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
#  ¿De cuántas maneras eres capaz de hacerlo?
#  Crea el código para cada una de ellas.
#

def iteration1():
    for i in range(1, 101):
        print(i)


def iteration2():
    counter = 1
    while counter <= 100:
        print(counter)
        counter = counter + 1


def iteration3(n):
    if n == 101:
        return
    else:
        print(n)
        iteration3(n + 1)


iteration3(1)
