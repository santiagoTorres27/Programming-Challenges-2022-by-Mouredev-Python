#
# Crea un programa que comprueba si los paréntesis, llaves y corchetes
# de una expresión están equilibrados.
# - Equilibrado significa que estos delimitadores se abren y cieran
#  en orden y de forma correcta.
# - Paréntesis, llaves y corchetes son igual de prioritarios.
#  No hay uno más importante que otro.
# - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# - Expresión no balanceada: { a * ( c + d ) ] - 5 }
#

import re

delimiters = {
    "(": ")",
    "[": "]",
    "{": "}"
}


def is_balanced_expression(expression: str):
    arr = re.findall(r"[\[\](){}]", expression)
    stack = []
    for i in arr:
        if i in delimiters:
            stack.append(i)
        else:
            if len(stack) > 0:
                top = stack[-1]
                if delimiters.get(top) == i:
                    stack.pop()
                else:
                    stack.append(i)
    return len(stack) == 0


my_expression = "{ [ a * ( c + d ) ] - 5 }"
my_expression2 = "{ a * ( c + d ) ] - 5 }"

print(is_balanced_expression(my_expression))
print(is_balanced_expression(my_expression2))
