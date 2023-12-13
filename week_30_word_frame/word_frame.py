#
# Crea una función que reciba un texto y muestre cada palabra en una línea,
# formando un marco rectangular de asteriscos.
# - ¿Qué te parece el reto? Se vería así:
#  **********
#  * ¿Qué   *
#  * te     *
#  * parece *
#  * el     *
#  * reto?  *
#  **********
#

import re


def find_greatest_length(text_arr):
    return max(len(word) for word in text_arr)


def make_words_frame(text: str):
    text_arr = re.split("\\s+", text)
    greatest_length = find_greatest_length(text_arr)
    text_arr.insert(0, "")
    text_arr.append("")

    for i in range(len(text_arr)):
        if i == 0 or i == len(text_arr) - 1:
            for _ in range(greatest_length + 4):
                print("*", end="")
            print()
        else:
            blank_spaces = greatest_length - len(text_arr[i])
            print(f"* {text_arr[i]}", end="")
            for _ in range(blank_spaces):
                print(" ", end="")
            print(" *")


my_text = "¿Que te parece el reto?"
make_words_frame(my_text)
