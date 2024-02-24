# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот.

# Например, 220 и 284 – дружественные числа.
# Выведите все пары дружественных чисел в диапазоне до 10000

import time


def sum_of_dev(numb):
    return sum([i for i in range(1, numb) if numb % i == 0])


def find_friendly(lim):
    full_list = []
    for numb in range(1, lim):
        sum_of_divisors = sum([i for i in range(1, numb) if numb % i == 0])
        if sum_of_divisors > 1 and sum_of_divisors != numb:
            full_list.append([numb, sum_of_divisors])
    # print(full_list)
    for item in full_list:
        if item[::-1] in full_list:
            full_list.remove(item[::-1])
            print(item)


if __name__ == '__main__':
    k = 3000

    start_time = time.time()
    for num in range(1, k):
        sum_current_num = sum_of_dev(num)
        if num < sum_current_num and sum_of_dev(sum_current_num) == num:
            print(num, sum_current_num)
    print("Решение 1: %s сек." % (time.time() - start_time))
    # k = 3000   0.195 сек
    # k = 18500  8.045 сек
    # k = 30000  21.15 сек

    start_time = time.time()
    find_friendly(k)
    print("Решение 2: %s сек." % (time.time() - start_time))
    # k = 3000   0.201 сек   + 3.076 %
    # k = 18500  8.658 сек   + 7.619 %
    # k = 30000  22.93 сек   + 8.416 %
