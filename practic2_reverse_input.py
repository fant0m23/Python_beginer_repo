# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном
# порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:  2 -> 3 4
# Output: 4 3


n = int(input("Введите количество элементов последовательности >>> "))


def reverse_input(n):
    element = input("Введите элемент последовательности >>> ")
    if n == 1:
        return f"{element} "
    else:
        return reverse_input(n - 1) + f"{element} "


print(reverse_input(n))
