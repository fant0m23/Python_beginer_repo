# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива.

from random import randint as ri


def get_list(size, min_val=0, max_val=10) -> list[int]:
    # my_list = []
    # for i in range(n):
    #     my_list.append(ri(min_val, max_val))
    # return my_list
    return [ri(min_val, max_val) for _ in range(size)]


def print_result(list_1, list_2):
    # new_list = []
    # for i in list_1:
    #     if i not in set(list_2) and i not in new_list:
    #         new_list.append(i)
    # return new_list
    return [i for i in list_1 if i not in set(list_2)]


if __name__ == "__main__":
    n = int(input("Введите количество элементов первого списка >>> "))
    k = int(input("Введите количество элементов второго списка >>> "))
    # list1 = get_list(n, 0, 7)
    # list2 = get_list(k, 0, 5)
    # print(list1)
    # print(list2)         -  это длинный вариант. Более короткий с "моржовым оператором" приведен ниже !
    #                         это синтаксический сахар позволяющий присвоить значение и сразу передать его в функцию
    print(list1 := get_list(n, 0, 7))
    print(list2 := get_list(k, 0, 5))
    print(print_result(list1, list2))
