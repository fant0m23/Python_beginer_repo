# Отсортируйте словарь по значению в порядке возрастания и убывания

import operator

if __name__ == '__main__':
    dict_1 = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'D': 2, 'G': 2,
              'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
              'Q': 10, 'Z': 10}

    # вариант 1
    result_rise = dict(sorted(dict_1.items(), key=operator.itemgetter(1)))
    result_wane = dict(sorted(dict_1.items(), key=operator.itemgetter(1), reverse=True))
    print("Вариант 1 (по возрастанию)")
    print(result_rise)
    print("\nВариант 1 (по убыванию)")
    print(result_wane)

    # вариант 2
    print("\nВариант 2 (сортировка по значениям)")

    for i in sorted(dict_1.items(), key=lambda func: func[1]):  # сортировка по значениям
        print(i, end=", ")

    print("")

    # вариант 3
    print("\nВариант 3 (сортировка по значениям, а затем и по ключам)")

    for i in sorted(dict_1.items(), key=lambda func: (func[1], func[0])):  # сорт-ка по значениям, а затем и по ключам
        print(i, end=", ")

    # вариант 4
    print("\n\nВариант 4 (сортировка списка со словарями по ключу age)")
    list_1 = [{'name': 'Jackie Chan', 'age': 70, 'salary': 10000},
              {'name': 'Ilon Mask', 'age': 53, 'salary': 55000},
              {'name': 'John McKain', 'age': 88, 'salary': 0}]

    for i in sorted(list_1, key=lambda func: func['age']):
        print(i)

    print("\nВариант 4 (сортировка списка со словарями по ключу salary)")  # аналогично и по "name"
    for i in sorted(list_1, key=lambda func: func['salary']):
        print(i)

