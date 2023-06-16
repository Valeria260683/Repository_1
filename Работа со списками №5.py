"""Напишите программу, которая суммирует все элементы в списке"""
def sum_list(items):
    sum_numbers = 0
    for i in items:
        sum_numbers += i
    return sum_numbers
items = [2, 3, 4, 5, 8]
print(sum_list(items))