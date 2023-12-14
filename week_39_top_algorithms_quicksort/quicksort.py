# Enunciado: Implementa uno de los algoritmos de ordenación más famosos:
#  el "Quick Sort", creado por C.A.R. Hoare.
# - Entender el funcionamiento de los algoritmos más utilizados de la historia
# Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
# Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
# - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
# donde trabajaremos y entenderemos los más famosos de la historia.
#


def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr, swap_index, i)
    swap(arr, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(arr, left, right):
    if left < right:
        pivot_index = pivot(arr, left, right)
        quick_sort_helper(arr, left, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, right)
    return arr


def quick_sort(numbers):
    return quick_sort_helper(numbers, 0, len(numbers) - 1)


my_numbers = [3, 5, 2, 4, -43, 0, 45, -3, -42]
print(quick_sort(my_numbers))
