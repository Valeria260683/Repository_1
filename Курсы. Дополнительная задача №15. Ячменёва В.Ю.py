"""Создать функцию, которая принимает список чисел и возвращает новый список, состоящий из квадратов чисел,
которые больше 10."""
def list_of_numbers(list):
    list_1 = []
    for n in list:
        if n > 10:
            list_1.append(n ** 2)


    return list_1
list = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15]
print(list_of_numbers(list))

