"""Напишите функцию, которая принимает список чисел и возвращает список квадратов этих чисел. """
def list_of_squares_numbers(list):
    list_1 = []
    for i in list:
        list_1.append(i ** 2)
    return list_1
list = [3, 5, 7, 9]
print(list_of_squares_numbers(list))
