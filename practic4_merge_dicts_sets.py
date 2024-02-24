# Программа для слияния нескольких словарей в один
def merge_dicts(dict1, dict2):
    dict_result = {}
    for i in dict1, dict2:  # в i на 1-й итерации записывается целиком сначала dict1, на 2-й - целиком dict2
        dict_result.update(i)
    return dict_result


def union_sets(set1, set2):
    set_result = set()
    for i in set1, set2:  # в i на 1-й итерации записывается целиком сначала set1, на 2-й - целиком set2
        set_result.update(i)
    return set_result


if __name__ == '__main__':
    dict_1 = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'D': 2, 'G': 2,
              'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8,
              'Q': 10, 'Z': 10}
    dict_2 = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'Д': 2,
              'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3, 'Й': 4, 'Ы': 4,
              'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Ф': 10, 'Щ': 10, 'Ъ': 10}
    # res_dict = merge_dicts(dict_1, dict_2)
    res_dict = {**dict_1, **dict_2}  # "звездочный" синтаксис объединения словарей
    print(len(res_dict), len(dict_1), len(dict_2))
    res_dict.update({'ЕУ': 356, 'ИИ': 345})
    print(res_dict['ЕУ'], res_dict['Q'])

    set_1 = {2, 5, 7, 2, 8}
    set_2 = {86, 136}
    print(set_1 | set_2)  # {2, 5, 86, 7, 8, 136}

    print(union_sets(set_1, set_2))

    for i in 1, "f", 3, True, 3.1484328:
        print(i)

    print(*set_1, *set_2)  # 8 2 5 7 136 86 --> вывод "звездочного" синтаксиса

# метод dict.fromkeys(keys, value) используется для создания словаря из множеств, списков
print("\n")
print("метод dict.fromkeys(keys, value) используется для создания словаря из множеств, списков\n")
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1, 2]

vowels = dict.fromkeys(keys, value)
print(vowels)

value.insert(1, 'ff')
print(vowels)
