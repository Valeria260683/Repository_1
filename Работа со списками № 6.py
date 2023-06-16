"""Напишите программу, которая умножает все элементы в списке"""
def multiplication_of_elements(lists):
    multiple = 1
    for i in lists:
        multiple *= i
    return multiple
lists = [2, 3, 6, 8]
print(multiplication_of_elements(lists))