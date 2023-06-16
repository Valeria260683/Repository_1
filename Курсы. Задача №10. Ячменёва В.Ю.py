"""Написать программу, которая может принимать любое неотрицательное целое число в качестве аргумента
и возвращать новое максимально возможное значение, составленное из цифр этого же числа.
По сути, просто переставить цифры, чтобы создать максимально возможное число."""
def max_number(num):
# Преобразуем число в список цифр
    num_list = list(str(num))
# Сортируем список в обратном порядке
    num_list.sort(reverse=True)
# Преобразуем список обратно в число
    max_num = int("".join(num_list))
    return max_num
print(max_number(12345))
print(max_number(8976543210))



