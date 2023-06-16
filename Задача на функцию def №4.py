"""Требуется создать функцию list_sort(list), которая сортирует
список чисел по убыванию их абсолютного значения."""
def list_sort(list):
    list.sort(key=lambda x: abs(x), reverse=True)
    return list
list = [-33, -0.05, -4.18, 11.20, 13.12, 55, 7.1]
print(list_sort(list))