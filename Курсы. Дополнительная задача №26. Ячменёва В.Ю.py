"""Напишите функцию, которая принимает на вход список чисел и возвращает True, если все числа
в списке положительные, и False в противном случае. """
def pozitive_negative_lists(my_lists):
    for x in my_lists:
        if x <= 0:
            return False
    return True
my_lists = [-3, -4, -5, 2, 6, 9, 12]
print(pozitive_negative_lists(my_lists))