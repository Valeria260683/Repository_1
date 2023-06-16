"""Напишите функцию, которая принимает два числа и возвращает результат
суммы целых чисел в этом диапазоне"""
def sum_numbers(a,b):
    if a < b:
        return sum(range(a, b+1))
    else:
        return sum(range(a, b+1))
print(sum_numbers(1, 10))







