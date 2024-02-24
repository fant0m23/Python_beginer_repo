# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Input: 5
# Output: yes
import math


def is_prime_number(n):
    for i in range(3, int(math.sqrt(n))):  # math.sqrt(n) можно было заменить на n ** 0.5
        if n % i == 0:
            print(i)
            return False

    return True


a = 51
print(is_prime_number(a))
